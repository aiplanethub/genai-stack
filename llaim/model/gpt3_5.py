import orjson
from langchain.schema import Generation
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

from llaim.model.base import BaseModel
from .prompts import BASIC_QA


class OpenAIGpt35Model(BaseModel):
    model_name = "Gpt_3.5"
    compulsory_fields = ["openai_api_key"]

    def load(self, model_path: str):
        return super().load(model_path)

    def predict(self, query: str):
        query = query.decode("utf-8")
        print(query)
        retriever_results = self.retriever.retrieve(query)
        
        # Manual chaining
        # prompt = BASIC_QA.format(context=retriever_results, user_prompt=query)
        # openai_chat = OpenAIChat(openai_api_key=self.model_config_fields.get("openai_api_key"), model="gpt-3.5-turbo")
        # response = openai_chat.generate(prompts=[prompt])
        # response = {
        #     "response": self.parse_generations(response.generations),
        #     "metadata": retriever_results,
        # }

        # Automatic chaining
        qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(
                model_name="gpt-3.5-turbo-16k",
                openai_api_key=self.model_config_fields.get("openai_api_key"),
                temperature=0,
            ),
            chain_type="stuff",
            chain_type_kwargs={"prompt": BASIC_QA},
            retriever=self.retriever.vectordb.get_langchain_client().as_retriever(),
            return_source_documents=True,
        )
        result = qa(query)
        print(result)
        return self.parse_qa_result(result)

    def parse_qa_result(self, qa_result: dict):
        parsed_result = {
            "query": qa_result["query"],
            "result": qa_result["result"],
            "source_documents": [
                {"content": document.page_content, "metadata": document.metadata}
                for document in qa_result["source_documents"]
            ],
        }
        return orjson.dumps(parsed_result)

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
