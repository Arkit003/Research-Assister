from langchain_core.documents import Document

def build_context(docs: list[Document]) -> str:
    """
    Converts retrieved docs into a single context string
    with page-aware citations.
    """
    context_blocks = []

    for doc in docs:
        page = doc.metadata.get("page")
        text = doc.page_content.strip()

        block = f"[Page {page}]\n{text}"
        context_blocks.append(block)

    return "\n\n".join(context_blocks)
