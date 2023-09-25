from .langchain import LangchainEmbedding


def get_default_embeddings():
    config = {
        "model_name": "sentence-transformers/all-mpnet-base-v2",
        "model_kwargs": {"device": "cpu"},
        "encode_kwargs": {"normalize_embeddings": False},
    }
    embedding = LangchainEmbedding.from_kwargs(name="HuggingFaceEmbeddings", fields=config)
    # Initialise the embedding
    embedding._post_init()
    return embedding
