import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

llm = LLM(
    model="openrouter/meta-llama/llama-3-8b-instruct",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)
