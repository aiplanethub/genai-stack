import os

from starlette.datastructures import UploadFile as StarletteUploadFile
from fastapi import UploadFile, Request


from genai_stack.genai_server.settings.settings import settings
from genai_stack.genai_server.models.etl_models import ETLJobRequestType
from genai_stack.genai_server.settings.config import stack_config
from genai_stack.constants.etl.platform import ETL_PLATFORM_MODULE, AVAILABLE_ETL_PLATFORMS
from genai_stack.utils.importing import import_class


# Default directories to store the job related data
DATA_DIR = "data"


class ETLUtil:
    def __init__(self, data: Request.form):
        self.data = data
        self.data_dir = os.path.join(settings.RUNTIME_PATH)
        self._setup_data_dir()

    def _setup_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir, exist_ok=True)

    def save_request(self, job_uuid: str):
        response = {}
        for key, value in self.data.items():
            if isinstance(value, (StarletteUploadFile, UploadFile)):
                file_path = os.path.join(self.data_dir, f"{job_uuid}.{self._get_ext(value.filename)}")
                with open(file_path, "wb") as f:
                    f.write(value.file.read())
                value = file_path
            response[key] = value
        return response

    def _get_ext(self, filename):
        return filename.split(".")[-1]


def get_etl_platform(**kwargs):
    etl_platform_config = stack_config.get("etl_platform")
    etl_platform, config = list(etl_platform_config.items())[0]

    cls_name = AVAILABLE_ETL_PLATFORMS.get(etl_platform)
    cls = import_class(f"{ETL_PLATFORM_MODULE}.{cls_name.replace('/', '.')}")

    return cls(platform_config=cls.config_class(**config), **kwargs)
