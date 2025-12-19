from fastapi import APIRouter, HTTPException
from app.schemas import HumanizeRequest, HumanizeResponse
from app.prompts import build_humanization_prompt
from app.llm import rewrite_text
from app.postprocess import postprocess_text

router = APIRouter()


@router.post("/humanize", response_model=HumanizeResponse)
def humanize_text(request: HumanizeRequest):
    try:
        prompt = build_humanization_prompt(request.text, request.tone)
        raw_output = rewrite_text(prompt)
        final_output = postprocess_text(raw_output)
        return HumanizeResponse(humanized_text=final_output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
