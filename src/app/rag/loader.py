from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_docs(path:Path)->str:
    '''
    Returns: docs and metadata
    '''
    reader = PyPDFLoader(path)
    documents = reader.load()
    
    
    return documents

def processed_pdf(path: Path):
    loader = PyPDFLoader(str(path))
    pages = loader.load()  

    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=800,
        chunk_overlap=150,
        separators=[
            "\n## ", "\n### ", "\n\n", "\n", " ", ""
        ]
    )

    chunks = splitter.split_documents(pages)

    return chunks