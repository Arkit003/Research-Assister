from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

def get_hf_embedding(device:str = "cpu"):


    model_name = "BAAI/bge-small-en-v1.5" #"BAAI/bge-large-en-v1.5"
    model_kwargs = {"device": device}
    encode_kwargs = {"normalize_embeddings": True}
    hf = HuggingFaceEmbeddings(
        model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
    )
    return hf


if __name__ == "__main__":
    hf = get_hf_embedding(device = "cuda")
    emb = hf.embed_query("hi i m arkit,i dont like it")
    print(len(emb))
    


    
    