from pydantic import BaseModel, Field


class HumanizeRequest(BaseModel):
    text: str = Field(..., min_length=20, description="AI-generated text to humanize")
    tone: str = Field(
        default="neutral",
        description="Tone of the rewritten text: neutral | casual | formal"
    )


class HumanizeResponse(BaseModel):
    humanized_text: str
