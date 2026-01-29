from app.rag.prompt import RAG_PROMPT
from app.rag.context import build_context
from app.exception.exception import CustomException
import sys

def run_rag_chain(llm, retriever, question: str):
    try:
        docs = retriever.invoke(
            "Represent this sentence for searching relevant passages: " + question
        )

        context = build_context(docs)

        messages = RAG_PROMPT.format_messages(
            context=context,
            question=question
        )

        response = llm.invoke(messages)
        #our custom llm returns a str rather than the reponse class through the groq key
        if isinstance(response, str):
            answer = response
        else:
            answer = response.content
        return answer, docs

    except Exception as e:
        raise CustomException(e, sys)
