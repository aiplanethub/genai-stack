from pydantic import BaseModel

from genai_stack.stack.stack import Stack
from genai_stack.etl.base import BaseETL


class BaseETLPlatformConfig(BaseModel):
    pass


class BaseETLPlatform:
    """
    ETL Platform is an interface that would run the ETL processes on workflow management to enable to scale the ETL workloads more efficiently.
    """

    def __init__(self, platform_config: BaseETLPlatformConfig, stack: Stack):
        self.platform_config = platform_config
        self.stack = stack
        self.setup()

    def setup(self):
        """
        Setup method to setup all the related things required to run the ETLPlatform
        """
        pass

    def handle_job(self, **kwargs):
        """
        A handler for incoming ETL jobs
        """
        raise NotImplementedError()
