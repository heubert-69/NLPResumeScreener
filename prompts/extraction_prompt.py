from langchain.prompts import PromptTemplate

extraction_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract the following from the resume:

- Skills
- Tools
- Experience (years + roles)

Rules:
- Only extract explicitly mentioned information
- Do NOT assume missing data

Return in JSON format.
Resume:
{resume}
"""
)
