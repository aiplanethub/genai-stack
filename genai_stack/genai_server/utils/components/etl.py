import os

from genai_stack.genai_server.settings import settings
from genai_stack.genai_server.models.etl_models import ETLJobRequestType

from starlette.datastructures import UploadFile as StarletteUploadFile
from fastapi import UploadFile


# Default directories to store the job related data
DATA_DIR = "data"


class ETLUtil:
    def __init__(self, data: ETLJobRequestType, job_id: int):
        self.data = ETLJobRequestType
        self.data_dir = os.path.join(settings.RUNTIME_PATH)
        self._setup_data_dir()

    def _setup_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir, exist_ok=True)

    def save_request(self, job_uuid: str):
        response = {}
        for key, value in self.data.dict():
            if isinstance(value, (StarletteUploadFile, UploadFile)):
                file_path = os.path.join(self.data_dir, f"{job_uuid}.{self._get_ext(value.filename)}")
                with open(file_path, "wb") as f:
                    f.write(value.file.read())
                value = file_path
            response[key] = file_path

    def _get_ext(self, filename):
        return filename.split(".")[-1]
