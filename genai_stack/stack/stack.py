class Stack:
    """GenAI Stack class

    GenAI stack class is a collection of multiple stack components that are
    required to run the stack. There are some compulsory components (model) and other components like
    (vectordb, retriever) that are required only if its needed by the user. 
    
    """
    def __init__(self, *, model, etl = None, vectordb = None, retriever = None, prompt_engine = None, response_evaluator = None) -> None:
        """Initializes and validates a stack instance.

        Args:
            model: Model component of the stack.
            etl: ETL component of the stack.
            vectordb: Vectordb component of the stack.
            retriever: Retriever component of the stack. 
            prompt_engine: PromptEngine component of the stack.
            response_evaluator: ResponseEvaluator component of the stack.
            
        """
        self._model = model
        self._etl = etl 
        self._vectordb = vectordb
        self._retriever = retriever 
        self._prompt_engine = prompt_engine
        self._response_evaluator = response_evaluator

    @property
    def model(self):
        """The Model of the stack.

        Returns:
            The Model of the stack.
        
        """
        return self._model
    

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
