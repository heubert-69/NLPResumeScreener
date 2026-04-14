from langchain.prompts import PromptTemplate

explanation_prompt = PromptTemplate(
    input_variables=["score", "match_data"],
    template="""
Explain why the candidate received this score.

Include:
- Strengths
- Weaknesses
- Missing skills

Score: {score}
Data: {match_data}
"""
)
