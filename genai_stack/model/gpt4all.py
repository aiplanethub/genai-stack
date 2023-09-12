import logging
import os
from pydantic import Field
from pathlib import Path
from typing import List, Optional, Union, Any
from gpt4all import GPT4All
from langchain.llms import GPT4All as LangChainGpt4aAll

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
