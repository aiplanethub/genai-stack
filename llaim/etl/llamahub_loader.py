from llaim.etl.base import EtlBase


class LLamaHubEtl(EtlBase):
    def __init__(self, name: str = "LLamaHubEtl", config: str = None) -> None:
        super().__init__(name, config)
