from typing import List, Union

from langchain.docstore.document import Document as LangDocument

from genai_stack.stack.stack import Stack


class Mediator:
    """This is the mediator class which handles all the intercomponent communication within a Stack.

    This is design pattern which allows for bidirectional communication between different components in the stack.
    Further reference: https://refactoring.guru/design-patterns/mediator/python/example
    """

    def __init__(self, stack: Stack):
        self._stack = stack

    def _is_component_available(self, component_name: str) -> bool:
        """
        This method is for checking the required component is available or not.

        Args:
            component_name:str
                Takes the component name

        Return:
            True or False
                True if component is available or False if None.
        """
        components = {
            "etl": self._stack.etl,
            "embedding": self._stack.embedding,
            "vectordb": self._stack.vectordb,
            "prompt_engine": self._stack.prompt_engine,
            "model": self._stack.model,
            "llm_cache": self._stack.llm_cache,
            "retriever": self._stack.retriever,
            "memory": self._stack.memory,
        }

        return bool(components.get(component_name))

    def _check_component(self, component: str, raise_error=False) -> None:
        if not self._is_component_available(component):
            component_name = component.title()
            if raise_error:
                raise ValueError(
                    f"Component {component_name} not found. Please add a {component_name} component to your stack"
                )
            else:
                print(f"Warning: {component_name} component not found.")
                return True
        return True

    # Embedding component
    def get_embedded_text(self, text):
        return self._stack.embedding.embed_text(text)

    def get_embedding_function(self):
        return self._stack.embedding.embedding

    def get_model_response(self, prompt: str) -> str:
        return self._stack.model.predict(prompt)

    # Memory component
    def add_text(self, user_text: str, model_text: str) -> None:
        if self._is_component_available("memory"):
            self._stack.memory.add_text(user_text, model_text)

    def get_chat_history(self) -> str:
        if self._is_component_available("memory"):
            return self._stack.memory.get_chat_history()

    # Vectordb
    def store_to_vectordb(self, documents: List[LangDocument]):
        if self._check_component("vectordb", raise_error=True):
            return self._stack.vectordb.add_documents(documents)

    def search_vectordb(self, query: str):
        if self._check_component("vectordb", raise_error=True):
            return self._stack.vectordb.search(query)

    def create_index(self, kwarg_map):
        if self._check_component("vectordb", raise_error=True):
            kwargs = kwarg_map.get(self._stack.vectordb.__class__.__name__)
            return self._stack.vectordb.create_index(**kwargs)

    def hybrid_search(self, query: str, metadata: dict, kwarg_map):
        if self._check_component("vectordb", raise_error=True):
            kwargs = kwarg_map.get(self._stack.vectordb.__class__.__name__)
            return self._stack.vectordb.hybrid_search(query, metadata, **kwargs)

    def get_documents(self, kwarg_map) -> Union[dict, None]:
        if self._check_component("vectordb", raise_error=True):
            kwargs = kwarg_map.get(self._stack.vectordb.__class__.__name__)
            return self._stack.vectordb.get_documents(**kwargs)

    def create_document(self, document, kwarg_map) -> dict:
        if self._check_component("vectordb", raise_error=True):
            kwargs = kwarg_map.get(self._stack.vectordb.__class__.__name__)
            return self._stack.vectordb.create_document(document, **kwargs)

    # LLM Cache
    def get_cache(self, query: str, metadata: dict = None):
        if self._is_component_available("llm_cache"):
            return self._stack.llm_cache.get_cache(query=query, metadata=metadata)
        return False

    def set_cache(self, query: str, response: str, metadata: dict = None):
        if self._is_component_available("llm_cache"):
            return self._stack.llm_cache.set_cache(
                metadata=metadata, query=query, response=response
            )
        return False

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
            raise ValueError(
                "VectorDB and Memory components are not provided, PromptEngine require at least anyone of it for the prompt template."
            )

    # Add more methods for inter component communication as we build the components
