import unittest
from pathlib import Path

from genai_stack.etl.langchain import list_langchain_loaders, LangchainETL
from genai_stack.etl.platform.prefect import PrefectETLPlatform, PrefectPlatformConfig
from genai_stack.embedding.utils import get_default_embeddings
from genai_stack.vectordb.chromadb import ChromaDB
from genai_stack.stack.stack import Stack


pdf_loader = LangchainETL.from_kwargs(name="PyPDFLoader", fields={})
csv_loader = LangchainETL.from_kwargs(name="CSVLoader", fields={})


print("PDF Loader id", pdf_loader.config.id)
print("CSV Loader id", csv_loader.config.id)


class TestEtl(unittest.TestCase):
    def setUp(self) -> None:
        self.embedding = get_default_embeddings()
        self.chromadb = ChromaDB.from_kwargs()

        print(self.embedding.get_config_data())

        self.etl_platform = PrefectETLPlatform(
            platform_config=Preembedding,
            vectordb=self.chromadb,
        )fectPlatformConfig(
                prefect_api_server="http://127.0.0.1:4200/api",
                runtime_path="/home/samjoel/Dphi/llaim/sandbox/private/etl_platform",
            ),
            loaders=[pdf_loader, csv_loader],
            embedding=self.

    def test_etl_platform(self):
        dir = Path("/home/samjoel/Dphi/datasets/data")
        for fp in list(dir.glob("*.pdf"))[:10]:
            self.etl_platform.handle_job(loader_id=pdf_loader.config.id, file_path=str(fp))


if __name__ == "__main__":
    unittest.main()
