class EtlBase:
    name: str
    config: str

    def __init__(self, name: str, config: str) -> None:
        super().__init__()

    def load_config(self):
        """This method is used for loading the configs from the file."""
        raise NotImplementedError

    def run(self):
        """This method should contain the actual logic for creating the EtL pipeline"""
        raise NotImplementedError
