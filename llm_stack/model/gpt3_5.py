from typing import List

from langchain.chains import RetrievalQA
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import Generation
from langchain.schema import Document


from fastapi.responses import JSONResponse
from llm_stack.model.base import BaseModel

from .prompts import BASIC_QA


class OpenAIGpt35Model(BaseModel):
    model_name = "Gpt_3.5"
    required_fields = ["openai_api_key"]
    response_class = JSONResponse

    def load(self, model_path: str):
        return super().load(model_path)

    def get_chat_history(self, *args, **kwargs):
        history = ""
        for argument in args:
            history += " \n " + argument
        return history

    def predict(self, query: str):
        query = query.decode("utf-8")
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo-16k",
            openai_api_key=self.model_config_fields.get("openai_api_key"),
            temperature=0,
        )

        # If Chat do a Conversation QA instead of Retrieval QA
        if self.model_config.get("chat", False):
            conversation_chain = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=self.retriever.get_langchain_retriever(),
                memory=self.get_memory(),
                get_chat_history=self.get_chat_history,
                return_source_documents=True,
            )
            results = conversation_chain({"question": query})
            print(results.keys())
            return self.parse_chat_result(results)
        else:
            qa = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                chain_type_kwargs={"prompt": BASIC_QA},
                retriever=self.retriever.get_langchain_retriever(),
                return_source_documents=True,
            )
            result = qa(query)
            return self.parse_qa_result(result)

    def _jsonify(self, result: dict) -> str:
        return json.dumps(result)
    def parse_chat_result(self, chat_result: dict):
        return {
            "result": chat_result["answer"],
            "source_documents": self._parse_source_documents(chat_result["source_documents"]),
        }

    def parse_qa_result(self, qa_result: dict):
        parsed_result = {
            "result": qa_result["result"],
            "source_documents": self._parse_source_documents(qa_result["source_documents"]),
        }
        return parsed_result

    def _parse_source_documents(self, source_documents: List[Document]):
        return [{"content": document.page_content, "metadata": document.metadata} for document in source_documents]

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
