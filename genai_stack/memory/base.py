from genai_stack.stack.stack_component import StackComponent

class BaseMemory(StackComponent):
    
    def get_user_text(self):
        """
        This method returns the user query
        """
        raise NotImplementedError()

    def get_model_text(self):
        """
        This method returns the model response
        """
        raise NotImplementedError()
    
    def get_text(self):
        """
        This method returns both user query and model response
        """
        raise NotImplementedError()
    
    def add_text(self):
        """
        This method stores both user query and model response
        """
        raise NotImplementedError()
    
    def get_chat_history(self):
        """
        This method returns the chat conversation history
        """
        raise NotImplementedError()