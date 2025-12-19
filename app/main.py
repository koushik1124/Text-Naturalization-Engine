from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router

app = FastAPI(
    title="Text Naturalization Engine",
    description="Improve the naturalness and readability of AI-generated text",
    version="1.0.0"
)

# ✅ CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # for local + demo use
    allow_credentials=True,
    allow_methods=["*"],      # allows OPTIONS, POST, etc.
    allow_headers=["*"],
)

app.include_router(router)
