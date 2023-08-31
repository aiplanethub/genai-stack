import contextlib
import json
import logging
import os
from pydantic import Field
from pathlib import Path
from typing import List, Optional, Union, Any

from gpt4all import GPT4All
from langchain import LLMChain, PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import GPT4All as LangChainGpt4aAll
from langchain.schema import Document, Generation

from genai_stack.model.base import BaseModel
from .base import BaseModelConfigModel, BaseModelConfig, BaseModel

logger = logging.getLogger(__name__)


class Gpt4AllParameters(BaseModelConfigModel):
    backend: Optional[str] = Field(None, alias="backend")

    max_tokens: int = Field(200, alias="max_tokens")
    """Token context window."""

    n_parts: int = Field(-1, alias="n_parts")
    """Number of parts to split the model into. 
    If -1, the number of parts is automatically determined."""

    seed: int = Field(0, alias="seed")
    """Seed. If -1, a random seed is used."""

    f16_kv: bool = Field(False, alias="f16_kv")
    """Use half-precision for key/value cache."""

    logits_all: bool = Field(False, alias="logits_all")
    """Return logits for all tokens, not just the last token."""

    vocab_only: bool = Field(False, alias="vocab_only")
    """Only load the vocabulary, no weights."""

    use_mlock: bool = Field(False, alias="use_mlock")
    """Force system to keep model in RAM."""

    embedding: bool = Field(False, alias="embedding")
    """Use embedding mode only."""

    n_threads: Optional[int] = Field(4, alias="n_threads")
    """Number of threads to use."""

    n_predict: Optional[int] = 256
    """The maximum number of tokens to generate."""

    temp: Optional[float] = 0.7
    """The temperature to use for sampling."""

    top_p: Optional[float] = 0.1
    """The top-p value to use for sampling."""

    top_k: Optional[int] = 40
    """The top-k value to use for sampling."""

    echo: Optional[bool] = False
    """Whether to echo the prompt."""

    stop: Optional[List[str]] = []
    """A list of strings to stop generation when encountered."""

    repeat_last_n: Optional[int] = 64
    "Last n tokens to penalize"

    repeat_penalty: Optional[float] = 1.18
    """The penalty to apply to repeated tokens."""

    n_batch: int = Field(8, alias="n_batch")
    """Batch size for prompt processing."""

    streaming: bool = False
    """Whether to stream the results or not."""

    allow_download: bool = False
    """If model does not exist in ~/.cache/gpt4all/, download it."""

    client: Any = None


class Gpt4AllModelConfigModel(BaseModelConfigModel):
    """
    Data Model for the configs
    """

    model: Optional[str] = "orca-mini-3b.ggmlv3.q4_0"
    model_path: Optional[Union[Path, str]] = "."
    parameters: Optional[Gpt4AllParameters]


class Gpt4AllModelConfig(BaseModelConfig):
    data_model = Gpt4AllModelConfigModel


class Gpt4AllModel(BaseModel):
    config_class = Gpt4AllModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()

    def load(self):
        cwd = os.getcwd()

        """
        Downloading the model weights
        """
        GPT4All.retrieve_model(model_name=self.config.model, model_path=self.config.model_path)
        abs_model_path = os.path.join(cwd, self.config.model_path, self.config.model)

        """
        Load the model
        """
        model = LangChainGpt4aAll(
            model=abs_model_path,
            **self.config.parameters,
        )
        return model

    def predict(self, prompt: str):
        response = self.model.predict(prompt)
        return {"output": response["result"]}


# class Gpt4AllModel(BaseModel):
#     model_name = "Gpt4All"
#     required_fields = []

#     def load(self, model_path: str = None):
#         model = "orca-mini-3b.ggmlv3.q4_0"
#         if getattr(self, "model_config_fields", None):
#             model = self.model_config_fields.get(
#                 "model",
#                 "orca-mini-3b.ggmlv3.q4_0",
#             )
#         model_path = Path(".")
#         cwd = os.getcwd()
#         GPT4All(model_name=model, model_path=str(model_path))
#         model_path = os.path.join(cwd, model_path, model)
#         logger.info(f"Model {model} at {model_path}")
#         self.model = LangChainGpt4aAll(
#             model=model_path,
#             max_tokens=self.model_config_fields.get("max_tokens", 2500),
#         )

#     def get_chat_history(self, *args, **kwargs):
#         return "".join(" \n " + argument for argument in args)

#     def predict(self, query: str):
#         query = self.preprocess(query)
#         llm = self.model

#         if getattr(self, "model_config", None) and self.model_config.get("chat", False):
#             return self._vector_retreiver_qa(llm, query)
#         elif self.retriever:
#             return self._vector_retreiver_qa(llm, query)
#         else:
#             return self._without_retreiver_qa(llm, query)

#     def _without_retreiver_qa(self, llm, query):
#         template = """Question: {question}

#             Answer: """

#         prompt = PromptTemplate(template=template, input_variables=["question"])
#         llm_chain = LLMChain(prompt=prompt, llm=llm)
#         question = query

#         return llm_chain.run(question)

#     def _vector_retreiver_qa(self, llm, query):
#         conversation_chain = ConversationalRetrievalChain.from_llm(
#             llm=llm,
#             retriever=self.retriever.get_langchain_retriever(),
#             memory=self.get_memory(),
#             get_chat_history=self.get_chat_history,
#             return_source_documents=True,
#         )
#         results = conversation_chain({"question": query})
#         return self.parse_chat_result(results)

#     def _jsonify(self, result: dict) -> str:
#         return json.dumps(result)

#     def parse_chat_result(self, chat_result: dict):
#         return {
#             "result": chat_result["answer"],
#             "source_documents": self._parse_source_documents(
#                 chat_result["source_documents"],
#             ),
#         }

#     def parse_qa_result(self, qa_result: dict):
#         return {
#             "result": qa_result["result"],
#             "source_documents": self._parse_source_documents(
#                 qa_result["source_documents"],
#             ),
#         }

#     def _parse_source_documents(self, source_documents: List[Document]):
#         return [
#             {
#                 "content": document.page_content,
#                 "metadata": document.metadata,
#             }
#             for document in source_documents
#         ]

#     def parse_generations(self, generation_lst: list):
#         """
#         Recursively parse the text in the generations
#         """
#         result = """"""

#         for g in generation_lst:
#             if isinstance(g, list):
#                 result += self.parse_generations(g)
#             if isinstance(g, Generation):
#                 result += g.text

#         return result
