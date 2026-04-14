AI Resume Screening System with LangChain + LangSmith

An end-to-end GenAI-powered Resume Screening System that evaluates candidates against a job description using LLMs, OCR, NLP preprocessing, and modular LangChain pipelines — with full LangSmith tracing for debugging and explainability.

---

Project Overview

This project simulates a real-world recruiter tool:

Input → Resume + Job Description
Process → Extraction → Matching → Scoring → Explanation
Output → Fit Score (0–100) + Justification

The system is designed to be:

- Modular
- Explainable
- Traceable (LangSmith)
- Production-inspired
- Key Features
- OCR Resume Parsing (PDF/Image support via Tesseract)
- Text Cleaning & NLP Preprocessing
- Regex cleaning
- Tokenization
- Stemming & Lemmatization
- LLM-Based Skill Extraction
🔍 Semantic Matching with Job Description
📊 Automated Scoring System (0–100)
💬 Explainable AI Output (Why this score?)
🔗 LangChain LCEL Pipelines
📈 LangSmith Tracing & Debugging

roject Structurre:
```bash
ai_resume_screening/
│
├── main.py
│
├── extractor/
│   ├── ocr_extractor.py
│   ├── pdf_extractor.py
│
├── preprocess/
│   ├── cleaner.py
│   ├── nlp_pipeline.py
│
├── prompts/
│   ├── extraction_prompt.py
│   ├── matching_prompt.py
│   ├── scoring_prompt.py
│   ├── explanation_prompt.py
│
├── chains/
│   ├── extraction_chain.py
│   ├── matching_chain.py
│   ├── scoring_chain.py
│   ├── explanation_chain.py
│
├── data/
│   ├── resumes/
│   ├── job_description.txt
│
├── utils/
│   ├── config.py
│   ├── helpers.py
│
├── requirements.txt

```
Pipeline Flow:
```bash
Resume → OCR Extraction → Text Cleaning → NLP Processing
       → Skill Extraction (LLM)
       → Matching (LLM)
       → Scoring (LLM)
       → Explanation (LLM)
       → LangSmith Tracing
```
---
Example Output
{
  "score": 85,
  "explanation": "The candidate demonstrates strong alignment with required skills such as Python, Machine Learning, and SQL. However, lacks experience in cloud deployment tools like AWS."
}
---
LangSmith Tracing (MANDATORY)

Tracing is enabled using:
```python
export LANGCHAIN_TRACING_V2=true
```

What’s Tracked:
- Skill Extraction
- Matching Logic
- Scoring Decisions
- Explanation Generation


Includes:
    3 Runs:
        - Strong Candidate
        - Average Candidate
        - Weak Candidate
        - Debugging incorrect outputs


---

Prompt Engineering Highlights:
- Strict no hallucination rules
- Structured JSON outputs
- Clear scoring constraints
- Explicit extraction boundaries

Example rule:

Do NOT assume skills not present in the resume

---

Tech Stack:

- Python
- LangChain (LCEL)
- LangSmith (Tracing & Debugging)
- OpenAI / HuggingFace APIs
- Pytesseract (OCR)
- NLTK (NLP preprocessing)
- Regex (re)

How to Run:
1. Clone the repo
```bash
git clone https://github.com/your-username/ai-resume-screening.git
cd NLPResume
```

2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Set environment variables
```bash
export OPENAI_API_KEY=your_key
export LANGCHAIN_TRACING_V2=true
```
4. Run the pipeline
```bash
python main.py
```

---
Evaluation Criteria Coverage
Criteria	Status
Pipeline Design	✅
LangChain Implementation	✅
Scoring Logic	✅
Explainability	✅
LangSmith Tracing	✅
Code Quality	✅
Bonus Features	✅

---
Future Improvements
- Embedding-based semantic similarity (FAISS)
- Dashboard UI (Streamlit/Gradio)
- Bulk resume processing
- Fine-tuned scoring model
- Recruiter analytics
