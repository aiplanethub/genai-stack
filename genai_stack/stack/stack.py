import uvicorn

from genai_stack.stack.utils import is_dir_exists, create_dir
from genai_stack.genai_server.server import get_genai_server_app
from genai_stack.genai_server.settings.config import read_configurations

class Stack:
    """GenAI Stack class

    GenAI stack class is a collection of multiple stack components that are
    required to run the stack. There are some compulsory components (model) and other components like
    (vectordb, retriever) that are required only if its needed by the user.

    """

    def __init__(
        self,
        *,
        model,
        embedding=None,
        etl=None,
        vectordb=None,
        llm_cache=None,
        retriever=None,
        prompt_engine=None,
        response_evaluator=None,
        memory=None
    ) -> None:
        """Initializes and validates a stack instance.

        Args:
            model: Model component of the stack.
            etl: ETL component of the stack.
            vectordb: Vectordb component of the stack.
            retriever: Retriever component of the stack.
            prompt_engine: PromptEngine component of the stack.
            response_evaluator: ResponseEvaluator component of the stack.
            memory: Memory component of the stack
        """
        self._model = model
        self._embedding = embedding
        self._etl = etl
        self._vectordb = vectordb
        self._llm_cache = llm_cache
        self._retriever = retriever
        self._prompt_engine = prompt_engine
        self._response_evaluator = response_evaluator
        self._memory = memory

        # Import here due to circular import conflict
        from genai_stack.stack.mediator import Mediator

        self._mediator = Mediator(stack=self)

        """
        Connect all components to the mediator. Post init of each component is called here. This is done to ensure
        that the mediator is available to all component's post init method.
        """
        if self._model:
            self._model.mediator = self._mediator
            self._model._post_init()
        if self._embedding:
            self._embedding.mediator = self._mediator
            self._embedding._post_init()
        if self._vectordb:
            self._vectordb.mediator = self._mediator
            self._vectordb._post_init()
        if self._etl:
            self._etl.mediator = self._mediator
            self._etl._post_init()
        if self._llm_cache:
            self._llm_cache.mediator = self._mediator
            self._llm_cache._post_init()
        if self._retriever:
            self._retriever.mediator = self._mediator
            self._retriever._post_init()
        if self._prompt_engine:
            self._prompt_engine.mediator = self._mediator
            self._prompt_engine._post_init()
        if self._response_evaluator:
            self._response_evaluator.mediator = self._mediator
            self._response_evaluator._post_init()
        if self._memory:
            self._memory.mediator = self._mediator
            self._memory._post_init()


    @property
    def model(self):
        """The Model of the stack.

        Returns:
            The Model of the stack.

        """
        return self._model

    @property
    def embedding(self):
        """The Embedding of the stack.

        Returns:
            The Embedding of the stack or None if the stack does not
            have a Embedding.
        """
        return self._embedding

    @property
    def etl(self):
        """The ETL of the stack.

        Returns:
            The ETL of the stack or None if the stack does not
            have a ETL.
        """
        self._etl

    @property
    def vectordb(self):
        """The Vectordb of the stack.

        Returns:
            The Vectordb of the stack or None if the stack does not
            have a Vectordb.
        """
        return self._vectordb

    @property
    def llm_cache(self):
        """The LLMCache of the stack.

        Returns:
            The LLMCache of the stack or None if the stack does not
            have a LLMCache.
        """
        return self._llm_cache

    @property
    def retriever(self):
        """The Retriever of the stack.

        Returns:
            The Retriever of the stack or None if the stack does not
            have a Retriever.
        """
        return self._retriever

    @property
    def prompt_engine(self):
        """The PromptEngine of the stack.

        Returns:
            The PromptEngine of the stack or None if the stack does not
            have a PromptEngine.
        """
        return self._prompt_engine

    @property
    def response_evaluator(self):
        """The ResponseEvaluator of the stack.

        Returns:
            The ResponseEvaluator of the stack or None if the stack does not
            have a ResponseEvaluator.
        """
        return self._response_evaluator

    @property
    def memory(self):
        """The Memory of the stack.

        Returns:
            The Memory of the stack or None if the stack does not
            have a Memory.
        """
        return self._memory
    
    @staticmethod
    def run_server(host:str = "127.0.0.1", port:int = 8000):
        """This method runs the Genai Server."""
        
        # if not is_dir_exists(run_time_path):
        #     create_dir(run_time_path)
        #     # create a stack_config.json with default configurations

        # read_configurations(run_time_path)

        app = get_genai_server_app()

        uvicorn.run(app=app, host=host, port=port)
