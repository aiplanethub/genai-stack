from llm_stack.constants.etl import PREBUILT_ETL_LOADERS, ETL_MODULE
from llm_stack.utils.importing import import_class

from llm_stack.config.loader import ConfigLoader


def list_etl_loaders():
    return PREBUILT_ETL_LOADERS.keys()


def run_etl_loader(config_file: str, vectordb):
    config_cls = ConfigLoader(name="EtlLoader", config=config_file)
    etl_cls = import_class(
        f"{ETL_MODULE}.{PREBUILT_ETL_LOADERS.get(config_cls.config.get('etl'))}".replace(
            "/",
            ".",
        )
    )
    etl = etl_cls(config=config_file, vectordb=vectordb)
    return etl.run()
