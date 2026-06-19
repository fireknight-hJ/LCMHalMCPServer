"""从 LangChain / ChatModel 返回的 AIMessage 上抽取 token usage（提供商字段名略有差异）。"""
from __future__ import annotations

from typing import Any, Dict, Optional


def extract_usage_from_message(msg: Any) -> Dict[str, Any]:
    """返回可 JSON 序列化的 usage 摘要；无则空 dict。"""
    out: Dict[str, Any] = {}
    if msg is None:
        return out

    um = getattr(msg, "usage_metadata", None)
    if isinstance(um, dict) and um:
        out["usage_metadata"] = dict(um)

    rm = getattr(msg, "response_metadata", None)
    if isinstance(rm, dict):
        tu = rm.get("token_usage")
        if isinstance(tu, dict) and tu:
            out["token_usage"] = dict(tu)

    return out


def sum_prompt_completion_tokens(usage_bundle: Dict[str, Any]) -> Optional[Dict[str, int]]:
    """尽力从 usage_metadata / token_usage 中归一为 prompt + completion 计数。"""
    if not usage_bundle:
        return None
    um = usage_bundle.get("usage_metadata") or {}
    tu = usage_bundle.get("token_usage") or {}
    # OpenAI-style
    pin = um.get("input_tokens") if isinstance(um, dict) else None
    cout = um.get("output_tokens") if isinstance(um, dict) else None
    if pin is None and isinstance(tu, dict):
        pin = tu.get("prompt_tokens")
    if cout is None and isinstance(tu, dict):
        cout = tu.get("completion_tokens")
    if pin is None and isinstance(um, dict):
        pin = um.get("prompt_tokens")
    if cout is None and isinstance(um, dict):
        cout = um.get("completion_tokens")
    try:
        pi = int(pin) if pin is not None else None
        co = int(cout) if cout is not None else None
    except (TypeError, ValueError):
        return None
    if pi is None and co is None:
        return None
    return {"prompt_tokens": pi or 0, "completion_tokens": co or 0}
