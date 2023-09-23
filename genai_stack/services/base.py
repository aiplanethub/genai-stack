from pydantic import BaseModel


class BaseServiceConfig(BaseModel):
    """
    Base service config to spawn a service
    """

    pass


class BaseService:
    config_class = BaseServiceConfig

    def __init__(self, **kwargs) -> None:
        self.config = self.config_class(**kwargs)

    def provision(self):
        """
        Method to provision the service
        """
        raise NotImplementedError()

    def deprovision(self):
        """
        Method to deprovision the service
        """
        raise NotImplementedError()

    def is_running(self):
        """
        Method to check if a service is running or not
        """
        raise NotImplementedError()

    def is_stopped(self):
        """
        Method to check if a service is running or not
        """
        raise NotImplementedError()

    def store_to_registry(self):
        """
        Method to store the service and its details to a ServiceRegistry
        """
        raise NotImplementedError()

    def get_status(self):
        """
        Get status of the service.
        """
        raise NotImplementedError()
