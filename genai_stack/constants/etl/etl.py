ETL_MODULE = "genai_stack.etl"


class LOADERS:
    LANGCHAIN = "langchain"
    LLAMA_HUB = "llama_hub"


AVAILABLE_ETL_LOADERS = {
    # loader : class name
    LOADERS.LANGCHAIN: "langchain/LangchainETL",
    LOADERS.LLAMA_HUB: "llamahub_loader/LLamaHubEtl",
}
