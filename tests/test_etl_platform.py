import unittest
from pathlib import Path

from genai_stack.etl.langchain import list_langchain_loaders, LangchainETL
from genai_stack.etl.platform.prefect import PrefectETLPlatform, PrefectPlatformConfig
from genai_stack.embedding.utils import get_default_embeddings
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.stack.stack import Stack


class TestEtl(unittest.TestCase):
    def setUp(self) -> None:
        self.etl_loader = LangchainETL.from_kwargs(name="PyPDFLoader", fields={"file_path": "/path/to/pdf"})
        self.embedding = get_default_embeddings()
        self.chromadb = ChromaDB.from_kwargs()

        self.stack = Stack(
            etl=self.etl_loader, embedding=self.embedding, vectordb=self.chromadb, model=None, run_etl=False
        )
        self.etl_platform = PrefectETLPlatform(
            platform_config=PrefectPlatformConfig(prefect_api_server="http://127.0.0.1:4200/api"), stack=self.stack
        )

    def test_etl_platform(self):
        dir = Path("/home/samjoel/Dphi/datasets/data")
        for fp in list(dir.glob("*.pdf"))[:10]:
            self.etl_platform.handle_job(file_path=str(fp))


if __name__ == "__main__":
    unittest.main()
