import os
import requests
from typing import Optional,List
from dotenv import load_dotenv
from langchain_core.language_models.llms import LLM

load_dotenv()
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

class CustomLLM(LLM):
    model: str = "gpt-4.1-mini"
    base_url: str = ""
    api_key: str = ""

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }

        r = requests.post(self.base_url, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]

    @property
    def _identifying_params(self):
        return {"model": self.model}

    @property
    def _llm_type(self):
        return "company-llm"
    
def get_llm():
    llm = CustomLLM(api_key=api_key,base_url=base_url)
    return llm