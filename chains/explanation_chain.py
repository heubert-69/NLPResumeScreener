from langchain_openai import ChatOpenAI
from prompts.explanation_prompt import explanation_prompt

llm = ChatOpenAI()

def run_explanation(score, match_data):
    chain = explanation_prompt | llm
    return chain.invoke({
        "score": score,
        "match_data": match_data
    })
