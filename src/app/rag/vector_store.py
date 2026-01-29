from pathlib import Path
from langchain_community.vectorstores import FAISS
from app.exception.exception import CustomException
import sys

VECTOR_DIR = Path("vectorstore/bge_large")


def build_vectorstore(documents, embeddings):
    try:
        vs = FAISS.from_documents(
            documents=documents,
            embedding=embeddings
        )
        VECTOR_DIR.mkdir(parents=True, exist_ok=True)
        vs.save_local(str(VECTOR_DIR))
        return vs
    except Exception as e:
        raise CustomException(e, sys)

def load_vectorstore(embeddings):
    if not VECTOR_DIR.exists():
        raise FileNotFoundError("Vectorstore not found. Rebuild index first.")

    try:
        return FAISS.load_local(
            str(VECTOR_DIR),
            embeddings,
            allow_dangerous_deserialization=True,
        )
    except Exception as e:
        raise CustomException(e, sys)


def add_documents(vectorstore, documents):
    try:
        vectorstore.add_documents(documents)
        vectorstore.save_local(str(VECTOR_DIR))
        return vectorstore
    except Exception as e:
        raise CustomException(e, sys)


def get_retriever(vectorstore, k=5):
    try:
        return vectorstore.as_retriever(search_kwargs={"k": k})
    except Exception as e:
        raise CustomException(e, sys)

BGE_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
def retrieve_docs(retriever, query: str):
    formatted_query = BGE_QUERY_PREFIX + query
    return retriever.invoke(formatted_query)

def log_docs(docs):
    for i, doc in enumerate(docs, 1):
        print(f"\nChunk {i}")
        print("Source:", doc.metadata.get("source"))
        print("Page  :", doc.metadata.get("page"))
        print("Text  :", doc.page_content[:300])
