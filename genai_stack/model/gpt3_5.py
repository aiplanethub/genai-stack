from typing import List, Optional, Union, Any, Dict, Tuple
from pydantic import Field

from langchain import LLMChain, PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import Generation, BaseMessage, SystemMessage, HumanMessage

from genai_stack.model.base import BaseModel, BaseModelConfig, BaseModelConfigModel


class OpenAIGpt35Parameters(BaseModelConfigModel):
    model_name: str = Field(default="gpt-3.5-turbo-16k", alias="model")
    """Model name to use."""
    temperature: float = 0
    """What sampling temperature to use."""
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Holds any model parameters valid for `create` call not explicitly specified."""
    openai_api_key: str
    """Base URL path for API requests, 
    leave blank if not using a proxy or service emulator."""
    openai_api_base: Optional[str] = None
    openai_organization: Optional[str] = None
    # to support explicit proxy for OpenAI
    openai_proxy: Optional[str] = None
    request_timeout: Optional[Union[float, Tuple[float, float]]] = None
    """Timeout for requests to OpenAI completion API. Default is 600 seconds."""
    max_retries: int = 6
    """Maximum number of retries to make when generating."""
    streaming: bool = False
    """Whether to stream the results or not."""
    n: int = 1
    """Number of chat completions to generate for each prompt."""
    max_tokens: Optional[int] = None
    """Maximum number of tokens to generate."""
    tiktoken_model_name: Optional[str] = None
    """The model name to pass to tiktoken when using this class. 
    Tiktoken is used to count the number of tokens in documents to constrain 
    them to be under a certain limit. By default, when set to None, this will 
    be the same as the embedding model name. However, there are some cases 
    where you may want to use this Embedding class with a model name not 
    supported by tiktoken. This can include when using Azure embeddings or 
    when using one of the many model providers that expose an OpenAI-like 
    API but with different models. In those cases, in order to avoid erroring 
    when tiktoken is called, you can specify a model name to use here."""


class OpenAIGpt35ModelConfigModel(BaseModelConfigModel):
    """
    Data Model for the configs
    """

    parameters: OpenAIGpt35Parameters


class OpenAIGpt35ModelConfig(BaseModelConfig):
    data_model = OpenAIGpt35ModelConfigModel


class OpenAIGpt35Model(BaseModel):
    config_class = OpenAIGpt35ModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()

    def load(self):
        """
        Using dict method here to dynamically access object attributes
        """
        model = ChatOpenAI(**self.config.parameters.dict())
        return model

    def predict(self, prompt: str):
        response = self.model.predict(prompt)
        return {"output": response}


# class OpenAIGpt35Model(BaseModel):
#     model_name = "Gpt_3.5"
#     required_fields = ["openai_api_key"]

#     def load(self, model_path: str):
#         self.model = ChatOpenAI(
#             model_name=self.model_config_fields.get("model_name", "gpt-3.5-turbo-16k"),
#             openai_api_key=self.model_config_fields.get("openai_api_key"),
#             temperature=0,
#         )

#     def parse_chat_history(self, *args, **kwargs):
#         return "".join(" \n " + argument for argument in args)

#     def predict(self, query: str):
#         query = self.preprocess(query)
#         llm = self.model

#         if self.model_config.get("chat", False):
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
#             get_chat_history=self.parse_chat_history,
#             return_source_documents=True,
#         )
#         results = conversation_chain({"question": query})
#         return self.parse_chat_result(results)

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
