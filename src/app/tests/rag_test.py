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

from app.models.cutsom_models import get_llm

load_dotenv()



def main():
    embeddings = get_hf_embedding()
    vectorstore = load_vectorstore(embeddings)
    retriever = get_retriever(vectorstore, k=5)

    llm = get_llm()

    question = "Explain batch normalization mathematically."
    answer, docs = run_rag_chain(llm, retriever, question)

    print("\nANSWER:\n", answer)

if __name__ == "__main__":
    main()
