from langchain_openai import ChatOpenAI
from prompts.scoring_prompt import scoring_prompt

llm = ChatOpenAI()

def run_scoring(match_data):
    chain = scoring_prompt | llm
    return chain.invoke({"match_data": match_data})
