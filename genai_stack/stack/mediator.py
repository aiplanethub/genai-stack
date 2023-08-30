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

    # Add more methods for inter component communication as we build the components
