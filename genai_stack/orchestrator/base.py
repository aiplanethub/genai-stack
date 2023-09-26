from pydantic import BaseModel


class BaseOrchestratorConfig(BaseModel):
    """"""

    pass


class BaseOrchestrator:
    """
    Class which is responsible for setting up the services on the desired infrastructure to run the Stack.
    """

    config_class = BaseOrchestratorConfig

    def __init__(self, **kwargs) -> None:
        self.config = self.config_class(**kwargs)

    def setup(self):
        """
        Setup the environment, directories or any other related stuff
        """
        raise NotImplementedError()
