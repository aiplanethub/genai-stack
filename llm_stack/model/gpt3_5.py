import json
from typing import List

from langchain import LLMChain, PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document, Generation

from llm_stack.model.base import BaseModel


class OpenAIGpt35Model(BaseModel):
    model_name = "Gpt_3.5"
    required_fields = ["openai_api_key"]

    def load(self, model_path: str):
        self.model = ChatOpenAI(
            model_name=self.model_config_fields.get("model_name", "gpt-3.5-turbo-16k"),
            openai_api_key=self.model_config_fields.get("openai_api_key"),
            temperature=0,
        )
        return super().load(model_path)

    def parse_chat_history(self, *args, **kwargs):
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
            get_chat_history=self.parse_chat_history,
            return_source_documents=True,
        )
        results = conversation_chain({"question": query})
        return self.parse_chat_result(results)

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
