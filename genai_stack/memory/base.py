from genai_stack.stack.stack_component import StackComponent

class BaseMemory(StackComponent):
    
    def add_user_text(self):
        """
        This method is for storing the user prompt in the memory
        """
        if not self.mediator._stack.vectordb:
            raise ValueError("VectorDB component is not provided, Memory component require a vectordb component.")
        
        vectorDB = self.mediator._stack.vectordb

        vectorDB.add_user_text(self.get_user_text())

    def add_model_text(self):
        """
        This method is for storing the model response in the memory
        """
        if not self.mediator._stack.vectordb:
            raise ValueError("VectorDB component is not provided, Memory component require a vectordb component.")
        
        vectorDB = self.mediator._stack.vectordb

        vectorDB.add_model_text(self.get_model_text())

    def get_user_text(self):
        """
        This method is for getting the user prompt
        """
        if not self.mediator._stack.prompt_engine:
            raise ValueError("Prompt Engine component is not provided, Memory component require a prompt engine component.")
        
        return self.mediator._stack.prompt_engine.get_prompt()

    def get_model_text(self):
        """
        This method is for getting the model response
        """
        if not self.mediator._stack.response_evaluator:
            raise ValueError("Response Evaluator component is not provided, Memory component require a response evaluator component.")
        
        return self.mediator._stack.response_evaluator.get_response()