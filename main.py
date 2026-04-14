import os

from extractor.pdf_extractor import extract_text_from_pdf
from preprocess.cleaner import clean_text
from preprocess.nlp_pipeline import preprocess_text

from chains.extraction_chain import run_extraction
from chains.matching_chain import run_matching
from chains.scoring_chain import run_scoring
from chains.explanation_chain import run_explanation


os.environ["LANGCHAIN_TRACING_V2"] = "true"


def pipeline(resume_path, job_description):

    # Step 1: Extract
    raw_text = extract_text_from_pdf(resume_path)

    # Step 2: Clean
    cleaned = clean_text(raw_text)

    # Step 3: NLP preprocess
    _ = preprocess_text(cleaned)

    # Step 4: LLM Extraction
    extracted = run_extraction(cleaned)

    # Step 5: Matching
    match = run_matching(extracted, job_description)

    # Step 6: Scoring
    score = run_scoring(match)

    # Step 7: Explanation
    explanation = run_explanation(score, match)

    return {
        "score": score,
        "explanation": explanation
    }


if __name__ == "__main__":
    with open("data/job_description.txt") as f:
        jd = f.read()

    result = pipeline("data/resumes/strong.pdf", jd)
    print(result)
