ETL_PLATFORM_MODULE = "genai_stack.etl.platform"


class ETLPlatforms:
    PREFECT = "prefect"


AVAILABLE_ETL_PLATFORMS = {
    # loader : class name
    ETLPlatforms.PREFECT: "prefect/PrefectETLPlatform",
}
