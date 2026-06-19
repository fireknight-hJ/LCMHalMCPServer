# Replacement code rubric checker.
# Uses an AI (LLM) with a prompt to validate replacement code generically (no hardcoded
# function lists). Used before persisting ReplacementUpdate and after FunctionClassifier output.

import re
from typing import Optional

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from config.model_singleton import get_model
from prompts.replacement_rubric_checker import (
    RUBRIC_CHECK_SYSTEM_PROMPT,
    RUBRIC_CHECK_USER_TEMPLATE,
    RUBRIC_CHECK_USER_TEMPLATE_WITH_ORIGINAL,
)


class RubricCheckResult(BaseModel):
    """Structured output from the AI rubric checker."""
    passed: bool = Field(description="True if the replacement is acceptable, false if it violates rubric rules.")
    reason: str = Field(default="", description="If passed is false, a short concrete reason for the author to fix. Empty if passed.")


def _looks_stub_like(code: str) -> bool:
    lines = [ln.strip() for ln in (code or "").splitlines() if ln.strip()]
    if not lines:
        return True
    significant = []
    for ln in lines:
        if ln.startswith("//") or ln.startswith("/*") or ln in ("{", "}",):
            continue
        # tolerate assert/cast-only scaffolding in stub-like replacements
        if re.search(r"\bassert\s*\(", ln):
            continue
        if re.search(r"^\(\s*void\s*\)\s*\w+\s*;", ln):
            continue
        significant.append(ln)
    if not significant:
        return True
    # pure return defaults are still stub-like for semantic checks
    if all(re.match(r"^return\b", s) for s in significant):
        return True
    return False


def _is_thin_wrapper_like(func_name: str, original_code: str) -> bool:
    """Heuristic: argument checks + small body + key delegate call."""
    orig = original_code or ""
    if not orig.strip():
        return False

    # Remove comments roughly to reduce noise for structural checks.
    no_line_comment = re.sub(r"//.*", "", orig)
    no_comment = re.sub(r"/\*.*?\*/", "", no_line_comment, flags=re.S)
    lines = [ln.strip() for ln in no_comment.splitlines() if ln.strip()]
    # too large -> likely not thin wrapper
    if len(lines) > 45:
        return False

    # control-flow richness check: thin wrappers usually have few branches and no loops
    loop_kw = len(re.findall(r"\b(for|while|do)\b", no_comment))
    if loop_kw > 0:
        return False

    # delegate call candidates (excluding self and language keywords)
    call_names = re.findall(r"\b([A-Za-z_]\w*)\s*\(", no_comment)
    excluded = {"if", "for", "while", "switch", "return", "sizeof", "assert"}
    delegates = [c for c in call_names if c not in excluded and c != func_name]
    if not delegates:
        return False

    # common thin-wrapper signs
    has_assert_or_guard = ("assert(" in no_comment) or ("if (" in no_comment) or ("if(" in no_comment)
    return has_assert_or_guard


def _deterministic_rules_check(func_name: str, replacement_code: str, original_code: Optional[str]) -> dict:
    """Fast fail-closed checks reused by VerifyReplacement path before LLM rubric."""
    repl = replacement_code or ""
    orig = original_code or ""
    if not repl.strip():
        return {"pass": True, "reason": ""}
    if not orig.strip():
        return {"pass": True, "reason": ""}

    # Rule 0 (hard reject): thin-wrapper should not be replaced by default.
    # Allow explicit override marker for rare evidence-backed exceptional cases.
    if _is_thin_wrapper_like(func_name, orig):
        if "ALLOW_THIN_WRAPPER_REPLACEMENT" not in repl:
            return {
                "pass": False,
                "reason": (
                    "Thin-wrapper function detected. Default policy: keep INIT wrapper original "
                    "(has_replacement=false). If replacement is truly required, provide explicit "
                    "evidence and include marker ALLOW_THIN_WRAPPER_REPLACEMENT."
                ),
            }

    # Rule A: thin-wrapper delegate call must not be dropped into stub.
    call_names = re.findall(r"\b([A-Za-z_]\w*)\s*\(", orig)
    # exclude language keywords / likely macros
    excluded = {
        "if", "for", "while", "switch", "return", "sizeof", "assert",
    }
    delegates = [c for c in call_names if c not in excluded and c != func_name]
    if delegates and _looks_stub_like(repl):
        has_delegate_in_repl = any(re.search(rf"\b{re.escape(d)}\s*\(", repl) for d in delegates)
        if not has_delegate_in_repl:
            return {
                "pass": False,
                "reason": (
                    f"Replacement removed key delegate call(s) {sorted(set(delegates))[:3]} "
                    "and became stub-like; violates shared INIT/semantic-preservation rules."
                ),
            }

    # Rule B: keep nextTcd address-domain conversion semantics when present.
    if ("nextTcd" in orig) and ("CONVERT_TO_DMA_ADDRESS" in orig):
        if ("nextTcd" not in repl) or ("CONVERT_TO_DMA_ADDRESS" not in repl):
            return {
                "pass": False,
                "reason": (
                    "Original contains nextTcd address-domain conversion semantics "
                    "(CONVERT_TO_DMA_ADDRESS); replacement dropped it."
                ),
            }
    return {"pass": True, "reason": ""}


def check_replacement_rubric(
    func_name: str,
    replacement_code: str,
    original_code: Optional[str] = None,
) -> dict:
    """
    Check replacement code against rubric rules:
    1) deterministic fail-fast checks for known high-risk semantic drops;
    2) AI rubric reviewer for broader semantic/CORE preservation checks.
    When original_code is provided, the reviewer compares original vs replacement and
    enforces e.g. that callers of CORE functions must preserve those calls.

    Args:
        func_name: Name of the function being replaced.
        replacement_code: The proposed replacement function body/source.
        original_code: Optional original source; if provided, included in the prompt so
            the reviewer can enforce caller-preservation and other rules.

    Returns:
        {"pass": bool, "reason": str}. If pass is False, reason describes what is wrong
        so the caller can feed it back to the AI for regeneration.
    """
    func_name = (func_name or "").strip()
    replacement_code = (replacement_code or "").strip()

    if not replacement_code:
        return {"pass": True, "reason": ""}

    deterministic = _deterministic_rules_check(func_name, replacement_code, original_code)
    if not deterministic.get("pass", True):
        return deterministic

    if original_code and (original_code or "").strip():
        user_content = RUBRIC_CHECK_USER_TEMPLATE_WITH_ORIGINAL.format(
            function_name=func_name,
            original_code=(original_code or "").strip(),
            replacement_code=replacement_code,
        )
    else:
        user_content = RUBRIC_CHECK_USER_TEMPLATE.format(
            function_name=func_name,
            replacement_code=replacement_code,
        )

    try:
        model = get_model()
        structured_model = model.with_structured_output(RubricCheckResult, method="json_mode")
        messages = [
            SystemMessage(content=RUBRIC_CHECK_SYSTEM_PROMPT),
            HumanMessage(content=user_content),
        ]
        result = structured_model.invoke(messages)
        if result is None:
            return {"pass": True, "reason": ""}
        if isinstance(result, dict):
            return {
                "pass": result.get("passed", True),
                "reason": result.get("reason") or "",
            }
        return {
            "pass": getattr(result, "passed", True),
            "reason": getattr(result, "reason", "") or "",
        }
    except Exception as e:
        # On LLM/network error, fail closed: reject the replacement so bad code is not persisted.
        # Caller can retry or fix; accepting on error allowed stub replacements to slip through.
        return {
            "pass": False,
            "reason": f"[Rubric check failed: {e!s}. Replacement not accepted to avoid persisting invalid code.]",
        }
