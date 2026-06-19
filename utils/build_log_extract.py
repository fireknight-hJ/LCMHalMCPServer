# 编译日志压缩提取：只保留错误/警告相关行及上下行，避免撑爆上下文

BUILD_LOG_MAX_CHARS = 12_000
LONG_LINE_MAX_CHARS = 600
# 每段匹配保留的「下文」行数（编译器常在 error 下一行打印源码片段，如 " 3286 | #if ..."）
CONTEXT_LINES_AFTER = 5


def _is_relevant(line: str) -> bool:
    """行是否与错误/失败相关（需保留）。"""
    lower = line.lower()
    return (
        "failed:" in lower
        or ": error" in lower
        or "error:" in lower
        or "fatal error" in lower
        or "undefined reference" in lower
        or ": warning" in lower
        or "warning:" in lower
        or "ninja: build" in lower
        or "编译失败" in line
    )


def _truncate_line(line: str, max_len: int = LONG_LINE_MAX_CHARS) -> str:
    if len(line) <= max_len:
        return line
    return line[:max_len] + "\n  ... [line truncated]"


def extract_build_errors(
    text: str,
    max_chars: int = BUILD_LOG_MAX_CHARS,
    context_before: int = 1,
    context_after: int = CONTEXT_LINES_AFTER,
) -> str:
    """从完整 build stdout/stderr 中提取与错误/警告相关的行，并限制总长度。

    - 匹配：FAILED、error:、fatal error、undefined reference、warning:、ninja: build 等。
    - 每段匹配保留「上一行」和「下一行」（或 context_after 行）作为上下文，便于保留
      编译器在 error 下方打印的源码片段（如 " 3286 | #if ..."）。
    - 单行过长则截断；总长超 max_chars 则保留尾部并注明省略。
    """
    if not (text or text.strip()):
        return ""
    lines = text.splitlines()
    if not lines:
        return ""

    collected: list[str] = []
    seen: set[str] = set()

    for i, line in enumerate(lines):
        if not _is_relevant(line):
            continue
        # 上文的 context_before 行
        for j in range(context_before, 0, -1):
            if i - j >= 0:
                prev = lines[i - j]
                if prev not in seen:
                    collected.append(_truncate_line(prev))
                    seen.add(prev)
        # 本行（匹配到的错误/失败行）
        if line not in seen:
            collected.append(_truncate_line(line))
            seen.add(line)
        # 下文的 context_after 行（编译器常在此打印源码片段）
        for j in range(1, context_after + 1):
            if i + j < len(lines):
                nxt = lines[i + j]
                if nxt not in seen:
                    collected.append(_truncate_line(nxt))
                    seen.add(nxt)

    result = "\n".join(collected).strip()
    if not result:
        result = "\n".join(lines[-50:])
    if len(result) > max_chars:
        result = "[... earlier build output omitted ...]\n\n" + result[-max_chars:]
    return result
