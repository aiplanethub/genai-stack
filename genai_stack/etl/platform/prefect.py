from pydantic import BaseModel

from .base import BaseETLPlatform


class PrefectPlatformConfig(BaseModel):
    prefect_api_server: str


class PrefectETLPlatform(BaseETLPlatform):
    config_class = PrefectPlatformConfig

    def handle_job(self, **kwargs):
        try:
            from prefect import flow
            from prefect.deployments import Deployment
        except ImportError:
            print(
                """
                Prefect is not found. Install prefect with "pip install prefect==2.10.21"
                """
            )

        @flow
        def process_job():
            self.stack.etl.run(**kwargs)

        deployment = Deployment.build_from_flow(process_job, name = "")
        deployment.apply()
