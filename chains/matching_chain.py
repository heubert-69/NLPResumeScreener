from langchain_openai import ChatOpenAI
from prompts.matching_prompt import matching_prompt

llm = ChatOpenAI()

def run_matching(resume_data, job_description):
    chain = matching_prompt | llm
    return chain.invoke({
        "resume_data": resume_data,
        "job_description": job_description
    })
