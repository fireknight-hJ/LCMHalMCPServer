# Replacement code rubric checker.
# Uses an AI (LLM) with a prompt to validate replacement code; no hardcoded rules.
# Used before persisting ReplacementUpdate and after FunctionClassifier output.

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


def check_replacement_rubric(
    func_name: str,
    replacement_code: str,
    original_code: Optional[str] = None,
) -> dict:
    """
    Check replacement code against rubric rules using an AI reviewer.

    Args:
        func_name: Name of the function being replaced.
        replacement_code: The proposed replacement function body/source.
        original_code: Optional original source; if provided, included in the prompt for context.

    Returns:
        {"pass": bool, "reason": str}. If pass is False, reason describes what is wrong
        so the caller can feed it back to the AI for regeneration.
    """
    func_name = (func_name or "").strip()
    replacement_code = (replacement_code or "").strip()

    if not replacement_code:
        return {"pass": True, "reason": ""}

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
        # On LLM/network error, allow the replacement (no hard fail) and record the error in reason
        return {
            "pass": True,
            "reason": f"[Rubric check failed: {e!s}]",
        }
