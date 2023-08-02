import json
from typing import List

from langchain import LLMChain, PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import GPT4All
from langchain.schema import Document, Generation

from llm_stack.model.base import BaseModel


class Gpt4AllModel(BaseModel):
    model_name = "Gpt4All"
    required_fields = []

    def load(self, model_path: str = None):
        model = "ggml-gpt4all-j-v1.3-groovy"
        if getattr(self, "model_config_fields", None):
            model = self.model_config_fields.get(
                "model",
                "ggml-gpt4all-j-v1.3-groovy",
            )
        self.model = GPT4All(
            model=model,
            max_tokens=2048,
        )

    def get_chat_history(self, *args, **kwargs):
        return "".join(" \n " + argument for argument in args)

    def predict(self, query: str):
        query = query.decode("utf-8")
        llm = self.model

        if self.model_config.get("chat", False):
            return self._vector_retreiver_qa(llm, query)
        elif self.retriever:
            return self._vector_retreiver_qa(llm, query)
        else:
            return self._without_retreiver_qa(llm, query)

    def _without_retreiver_qa(self, llm, query):
        template = """Question: {question}

            Answer: """

        prompt = PromptTemplate(template=template, input_variables=["question"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        question = query

        return llm_chain.run(question)

    def _vector_retreiver_qa(self, llm, query):
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=self.retriever.get_langchain_retriever(),
            memory=self.get_memory(),
            get_chat_history=self.get_chat_history,
            return_source_documents=True,
        )
        results = conversation_chain({"question": query})
        return self.parse_chat_result(results)

    def _jsonify(self, result: dict) -> str:
        return json.dumps(result)

    def parse_chat_result(self, chat_result: dict):
        return self._jsonify(
            {
                "result": chat_result["answer"],
                "source_documents": self._parse_source_documents(
                    chat_result["source_documents"],
                ),
            }
        )

    def parse_qa_result(self, qa_result: dict):
        return self._jsonify(
            {
                "result": qa_result["result"],
                "source_documents": self._parse_source_documents(
                    qa_result["source_documents"],
                ),
            }
        )

    def _parse_source_documents(self, source_documents: List[Document]):
        return [
            {
                "content": document.page_content,
                "metadata": document.metadata,
            }
            for document in source_documents
        ]

    def parse_generations(self, generation_lst: list):
        """
        Recursively parse the text in the generations
        """
        result = """"""

        for g in generation_lst:
            if isinstance(g, list):
                result += self.parse_generations(g)
            if isinstance(g, Generation):
                result += g.text

        return result