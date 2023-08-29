ETL_MODULE = "genai_stack.etl"


class LOADERS:
    LANGCHAIN = "langchain"
    LLAMA_HUB = "llama_hub"


PREBUILT_ETL_LOADERS = {
    # loader : class name
    LOADERS.LANGCHAIN: "lang_loader/LangLoaderEtl",
    LOADERS.LLAMA_HUB: "llamahub_loader/LLamaHubEtl",
}
