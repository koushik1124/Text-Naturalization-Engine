def build_humanization_prompt(text: str, tone: str) -> str:
    return f"""
Rewrite the following text so that it sounds naturally written by a human.

Guidelines:
- Preserve the original meaning
- Use varied sentence lengths
- Avoid repetitive or academic phrasing
- Maintain a {tone} tone
- Do NOT add new information

Text:
{text}
""".strip()
