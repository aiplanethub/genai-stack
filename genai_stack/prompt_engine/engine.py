from typing import Union

from genai_stack.prompt_engine.base import BasePromptEngine, BasePromptEngineConfigModel, BasePromptEngineConfig
from langchain.chains import OpenAIModerationChain


class PromptEngineConfigModel(BasePromptEngineConfigModel):
    chat_history_prompt: str = """
    The following is a conversation between you and human. If you don't know the answer, just say that you don't know,
    don't try to make up an answer.

    Current conversations:
    {history}
    human: {input}
    you:
    """
    chat_context_prompt: str = """
    The following is a conversation between you and human. Use the following pieces of context to complete the
    conversation. If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Please provide an answer which is factually correct and based on the information given in the context.
    Mention any quotes supporting the answer if it's present in the context which is delimited by four # characters.
    ####{context}####

    Current conversations:
    {history}
    human: {input}
    you:
    """
    context_prompt: str = """
    Use the following pieces of context to answer the question. Question is delimited by triple backticks (```). If you
    don't know the answer, just say that you don't know, don't try to make up an answer. Please provide an answer which
    is factually correct and based on the information from the context. Mention any quotes supporting the answer if it's
    present in the context which is delimited by four # characters
    ####{context}####

    human:```{question}```
    you:
    """
    shouldValidate: bool = True
    openai_api_key: str = ""


class PromptEngineConfig(BasePromptEngineConfig):
    data_model = PromptEngineConfigModel


class PromptEngine(BasePromptEngine):
    config_class = PromptEngineConfig

    def __init__(self, llm, **kwargs):
        super().__init__(llm, **kwargs)
        self.moderation_chain = OpenAIModerationChain(
            openai_api_key=self.config.openai_api_key,
            error=True
        )

    def validate_prompt(self, prompt: str) -> Union[bool, None]:
        """
        This method validates the prompt using the OpenAI Moderation API. If the prompt is valid, it returns True,
        """
        if not self.config.shouldValidate:
            return None
        try:
            self.moderation_chain.run(prompt)
        except ValueError:
            return False
        return True
