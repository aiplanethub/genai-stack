import json
import requests
import logging
from urllib.parse import urljoin
from requests.auth import _basic_auth_str
from pathlib import Path
from uuid import uuid4
from typing import Optional

from .base import BaseETL, BaseETLConfig, BaseETLConfigModel
from .exception import LLMStackEtlException


class AirbyteAuth:
    api_key = Optional[str] = None
    username: Optional[str] = "airbyte"
    password: Optional[str] = "password"


class AirbyteConfiguration:
    configuration: dict


class AirbyteETLConfigModel(BaseETLConfigModel):
    host: str
    "host: A string which contains the host of the airbyte"

    workspace_id: Optional[str] = None
    "workspace_id: An optional string which contains the workspace id of the airbyte"

    auth: Optional[AirbyteAuth] = AirbyteAuth()
    source: AirbyteConfiguration
    destination: AirbyteConfiguration


class AirbyteETLConfig(BaseETLConfig):
    data_model = AirbyteETLConfigModel


class AirbyteETL(BaseETL):
    """Airbyte ETL Class

    The class which creates sources, destinations and connections in Airbyte to execute the ETL Process.
    """

    config_class = AirbyteETLConfig

    @property
    def workspace_id(self):
        return self.config.workspace_id or self._create_workspace_id()

    @property
    def _auth_header(self):
        header = {}
        api_key = self.config.auth.api_key

        if api_key:
            header["Authorization"] = f"Bearer {api_key}".strip()
        else:
            header["Authorization"] = f"Bearer {api_key}".strip()
            encoded_auth = _basic_auth_str(
                username=self.config.auth.username,
                password=self.config.auth.password,
            )
            header["Authorization"] = encoded_auth
        return header

    @property
    def _headers(self):
        return self._auth_header

    def _get_airbyte_url(self, url_path: str):
        return urljoin(self.config.host, url_path)

    def _create_source(self):
        data = {"configuration": self.config.source.configuration, "workspaceId": self.workspace_id}
        response = self._call_airbyte_api(method="post", url="/api/v1/sources/create", data=data)
        self.source_id = response.get("sourceId")
        return response

    def _create_destination(self):
        data = {"configuration": self.config.destination.configuration, "workspaceId": self.workspace_id}
        response = self._call_airbyte_api(method="post", url="/api/v1/destinations/create", data=data)
        self.destination_id = response.get("destinationId")
        return response

    def _call_airbyte_api(self, method: str, url: str, data: dict = None, query_params: dict = None):
        response = getattr(requests, method)(url=url, headers=self._headers, json=data, params=query_params)
        if not response.ok:
            raise LLMStackEtlException(f"Exception: {response.text}")
        return response.json()

    def _create_connection(self):
        data = {
            "prefix": "genai_stack",
            "sourceId": self.source_id,
            "destinationId": self.destination_id,
            "status": "active",
        }
        response = self._call_airbyte_api("post", url="/api/v1/connections/create", data=data)
        json_response = response.json()
        self.connection_id = json_response["connectionId"]
        print(f"Connection was created - {self.connection_id}")
        return json_response

    def _create_workspace_id(self):
        """If a workspace_id is not provided in the config.json, it will be created."""
        data = {"name": uuid4().hex}

        response = self._call_airbyte_api("post", url="/api/v1/workspaces/create", data=data)
        print(f'Created Workspace - {response.json().get("workspaceId")}')

        return response.json().get("workspaceId")

    def source_definitions_list(self):
        response = self._call_airbyte_api("get", url="/api/v1/source_definitions/list")
        return response.get("data")

    def destination_definitions_list(self):
        response = self._call_airbyte_api("get", url="/api/v1/destination_definitions/list")
        return response.get("data")

    def run(self):
        self._create_source()
        self._create_destination()
        self._create_connection()
