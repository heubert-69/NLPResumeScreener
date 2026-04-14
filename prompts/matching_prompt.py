from langchain.prompts import PromptTemplate

matching_prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
Compare the resume data with the job description.

Identify:
- Matching skills
- Missing skills

Return structured JSON.

Resume:
{resume_data}

Job:
{job_description}
"""
)
