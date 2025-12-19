import re

AI_PHRASES = [
    "in conclusion",
    "overall,",
    "moreover,",
    "additionally,",
    "it is important to note that",
    "this clearly shows that",
    "as an ai",
]


def clean_whitespace(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def remove_ai_phrases(text: str) -> str:
    lowered = text.lower()
    for phrase in AI_PHRASES:
        lowered = lowered.replace(phrase, "")
    return lowered


def normalize_sentences(text: str) -> str:
    # Ensure space after punctuation
    text = re.sub(r"([.!?])([A-Za-z])", r"\1 \2", text)
    return text


def postprocess_text(text: str) -> str:
    text = clean_whitespace(text)
    text = remove_ai_phrases(text)
    text = normalize_sentences(text)
    return text
