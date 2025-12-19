🧠 Text Naturalization Engine

A production-oriented AI backend application that improves the naturalness, readability, and human-like flow of AI-generated text using Large Language Models (LLMs) combined with deterministic post-processing.

This project focuses on applied NLP system design, not gimmicks — combining probabilistic LLM outputs with rule-based control for consistent, explainable results.

🚀 Project Overview

Modern AI systems generate text quickly, but the output often sounds repetitive, robotic, or overly generic.
The Text Naturalization Engine addresses this problem by rewriting AI-generated content to make it sound more natural and human-written while preserving the original meaning.

The system is designed as a clean backend service with a lightweight frontend for demonstration.

🎯 Key Features

✍️ AI-Assisted Text Rewriting
Uses Groq-hosted LLMs to rewrite text with improved flow and clarity.

🧩 Prompt-Engineered Control
Dedicated prompt templates ensure consistent rewriting behavior and tone control.

🛠️ Deterministic Post-Processing
Rule-based cleanup layer removes common AI artifacts and normalizes sentence structure.

🎛️ Tone Selection
Supports neutral, casual, and formal rewriting styles.

⚙️ Clean Backend Architecture
Modular FastAPI design with clear separation of concerns.

🌐 Lightweight Frontend Demo
Simple HTML/CSS/JS interface for easy testing and demonstration.

🏗️ System Architecture
User Input
   ↓
FastAPI Backend
   ↓
Prompt Engineering Layer
   ↓
Groq LLM (Text Rewriting)
   ↓
Post-Processing Rules
   ↓
Humanized Output


This hybrid design ensures:

Flexibility from LLMs

Consistency from deterministic logic

Explainability at each step

🛠️ Tech Stack

Language: Python

Backend Framework: FastAPI

LLM Provider: Groq

NLP: Prompt engineering + rule-based post-processing

Frontend: HTML, CSS, JavaScript

API Format: REST (JSON)

📁 Project Structure
```text
text-naturalization-engine/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── api.py           # API routes
│   ├── llm.py           # Groq LLM integration
│   ├── prompts.py       # Prompt templates
│   ├── postprocess.py   # Deterministic text cleanup
│   └── schemas.py       # Request/response models
│
├── frontend/
│   ├── index.html       # Demo UI
│   ├── style.css
│   └── script.js
│
├── .env.example
├── requirements.txt
└── README.md
```
⚙️ Setup & Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/text-naturalization-engine.git
cd text-naturalization-engine

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here

5️⃣ Run the backend
uvicorn app.main:app --reload

6️⃣ Run the frontend

Open:

frontend/index.html


in your browser.

📌 API Usage Example

Endpoint: POST /humanize

Request:

{
  "text": "This is an AI generated paragraph that sounds very generic and robotic.",
  "tone": "casual"
}


Response:

{
  "humanized_text": "So you want to know about this AI-generated paragraph. It feels generic and robotic, lacking any real personality or natural flow."
}

🧠 Design Philosophy

This project intentionally prioritizes:

Readability over raw generation

Explainability over black-box behavior

System design over one-off prompts

Ethical AI usage over detection bypass claims

The goal is to demonstrate how AI systems can be engineered responsibly for real-world use.

📈 Future Enhancements

Readability scoring and metrics

Sentence-level variance analysis

Authentication & rate limiting

Deployment with public demo URL

Logging and monitoring for output quality

👤 Author

Koushik Yadagiri
AI Engineer | Backend & Applied NLP Systems

🔗 GitHub: https://github.com/koushik1124

🔗 LinkedIn: https://www.linkedin.com/in/koushik-yadagiri-bb3a14218

⚠️ Disclaimer

This project is intended to improve text quality and readability.
It does not claim to bypass AI detection systems or guarantee human authorship.