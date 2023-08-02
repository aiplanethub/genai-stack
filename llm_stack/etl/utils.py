import typing

from langchain.document_loaders import JSONLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import WebBaseLoader


class FileDataSources:
    CSV = "csv"
    PDF = "pdf"
    WEB = "web"
    JSON = "json"
    MARKDOWN = "markdown"


FILE_DATA_SOURCES_MAP = {
    FileDataSources.CSV: {"loader": CSVLoader, "default_kwarg": "file_path"},
    FileDataSources.PDF: {"loader": PyPDFLoader, "default_kwarg": "file_path"},
    FileDataSources.WEB: {"loader": WebBaseLoader, "default_kwarg": "web_path"},
    FileDataSources.JSON: {"loader": JSONLoader, "default_kwarg": "file_path"},
    FileDataSources.MARKDOWN: {"loader": UnstructuredMarkdownLoader, "default_kwarg": "file_path"},
}


def get_config_from_source_kwargs(source_type: str, source: typing.Union[str, dict]):
    source_map = FILE_DATA_SOURCES_MAP[source_type]
    fields = {}

    if isinstance(source, str):
        fields[source_map["default_kwarg"]] = source
    elif isinstance(source, dict):
        fields.update(source)

    return {"source": {"name": source_map["loader"].__name__, "fields": fields}}
