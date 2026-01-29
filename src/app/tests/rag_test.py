from app.rag.vector_store import load_vectorstore
from app.rag.embedding import get_hf_embedding
from app.rag.vector_store import get_retriever
from app.rag.chain import run_rag_chain
# from langchain_openai import ChatOpenAI
import requests
from typing import Optional,List
from langchain_core.language_models.llms import LLM
from dotenv import load_dotenv
import os

load_dotenv()

class CustomLLM(LLM):
    model: str = "gpt-4.1-mini"
    base_url: str = "https://api.manus.im/api/llm-proxy/v1/chat/completions"
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
    
api_key = os.getenv("API_KEY")

def main():
    embeddings = get_hf_embedding()
    vectorstore = load_vectorstore(embeddings)
    retriever = get_retriever(vectorstore, k=5)

    llm = CustomLLM(api_key=api_key)

    question = "Explain batch normalization mathematically."
    answer, docs = run_rag_chain(llm, retriever, question)

    print("\nANSWER:\n", answer)

if __name__ == "__main__":
    main()
