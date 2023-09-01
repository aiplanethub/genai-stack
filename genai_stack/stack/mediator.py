from genai_stack.stack.stack import Stack


class Mediator:
    """This is the mediator class which handles all the intercomponent communication within a Stack.

    This is design pattern which allows for bidirectional communication between different components in the stack.
    Further reference: https://refactoring.guru/design-patterns/mediator/python/example
    """

    def __init__(self, stack: Stack):
        self._stack = stack

    # Embedding component
    def get_embedded_text(self, text):
        return self._stack.embedding.embed_text(text)

    def get_model_response(self, prompt: str) -> str:
        return self._stack.model.predict(prompt)

    # Prompt Engine
    def get_prompt_template(self, query: str):
        if self._stack.vectordb and self._stack.memory:
            return self._stack.prompt_engine.get_prompt_template(
                query=query, promptType="CONTEXTUAL_CHAT_PROMPT"
            )
        elif self._stack.memory:
            return self._stack.prompt_engine.get_prompt_template(
                query=query, promptType="SIMPLE_CHAT_PROMPT"
            )
        elif self._stack.vectordb:
            return self._stack.prompt_engine.get_prompt_template(
                query=query, promptType="CONTEXTUAL_QA_PROMPT"
            )
        else:
            raise ValueError("VectorDB and Memory components are not provided, PromptEngine require atleast anyone of it for the prompt template.")

    # Add more methods for inter component communication as we build the components
