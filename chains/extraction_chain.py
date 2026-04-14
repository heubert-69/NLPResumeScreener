from langchain_openai import ChatOpenAI
from prompts.extraction_prompt import extraction_prompt

llm = ChatOpenAI()

def run_extraction(resume_text):
    chain = extraction_prompt | llm
    return chain.invoke({"resume": resume_text})
