from typing import Optional, Dict

import torch
from langchain import LLMChain, PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFacePipeline
from langchain.schema import Document, Generation

from genai_stack.model.base import BaseModel, BaseModelConfig, BaseModelConfigModel


class HuggingFaceModelConfigModel(BaseModelConfigModel):
    """
    Data Model for the configs
    """

    model: Optional[str] = "nomic-ai/gpt4all-j"
    """Model name to use."""
    model_kwargs: Optional[Dict] = None
    """Key word arguments passed to the model."""
    pipeline_kwargs: Optional[dict] = None
    """Key word arguments passed to the pipeline."""
    task: str = "text-generation"
    """Valid tasks: 'text2text-generation', 'text-generation', 'summarization'"""


class HuggingFaceModelConfig(BaseModelConfig):
    data_model = HuggingFaceModelConfigModel


class HuggingFaceModel(BaseModel):
    config_class = HuggingFaceModelConfig

    def _post_init(self, *args, **kwargs):
        self.model = self.load()

    def get_device(self):
        return torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

    def load(self):
        model = HuggingFacePipeline.from_model_id(
            model_id=self.config.model,
            task=self.config.task,
            model_kwargs=self.config.model_kwargs,
            device=self.get_device(),
        )
        return model

    def predict(self, prompt: str):
        response = self.model(prompt)
        return {"output": response[0]["generated_text"]}


# class HuggingFaceModel(BaseModel):
#     model_name = "hf"
#     required_fields = []

#     def load(self, model_path: str = None):
#         model = "nomic-ai/gpt4all-j"
#         if getattr(self, "model_config_fields", None):
#             model = self.model_config_fields.get(
#                 "repo_id",
#                 "nomic-ai/gpt4all-j",
#             )
#         self.model = HuggingFacePipeline.from_model_id(
#             model_id=model,
#             task=self.model_config_fields.get("task", "text-generation"),
#             model_kwargs=self.model_config_fields.get("model_kwargs"),
# device=self.get_device(),
#         )

#     def get_chat_history(self, *args, **kwargs):
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
#             get_chat_history=self.get_chat_history,
#             return_source_documents=True,
#         )
#         results = conversation_chain({"question": query})
#         return self.parse_chat_result(results)

#     def _jsonify(self, result: dict) -> str:
#         return json.dumps(result)

#     def parse_chat_result(self, chat_result: dict):
#         return self._jsonify(
#             {
#                 "result": chat_result["answer"],
#                 "source_documents": self._parse_source_documents(
#                     chat_result["source_documents"],
#                 ),
#             }
#         )

#     def parse_qa_result(self, qa_result: dict):
#         return self._jsonify(
#             {
#                 "result": qa_result["result"],
#                 "source_documents": self._parse_source_documents(
#                     qa_result["source_documents"],
#                 ),
#             }
#         )

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
