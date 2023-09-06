# 📖 Advanced Usage

## Create your own Custom Retriever Component

Each stack component has three Base Interfaces.

Base Interfaces for the Retriever component

```py
class BaseRetrieverConfigModel(BaseModel):
    """
    Data Model for the configs
    """
    pass


class BaseRetrieverConfig(StackComponentConfig):
    data_model = BaseRetrieverConfigModel


class BaseRetriever(StackComponent):
    config_class = BaseRetrieverConfig

    def get_prompt(self, query:str):
        """
        This method returns the prompt template from the prompt engine component
        """
        return self.mediator.get_prompt_template(query)

    def retrieve(self, query:str) -> dict:
        """
        This method returns the model response for the prompt template.
        """
        raise NotImplementedError()

    def get_context(self, query:str):
        """
        This method returns the relevant documents returned by the similarity search from a vectordb based on the query
        """
        raise NotImplementedError()

    def get_chat_history(self) -> str:
        """
        This method returns the chat conversation history
        """
        return self.mediator.get_chat_history()
```

**1. Creating a Custom Retriever Component**: Create a new class that extends the BaseRetriever class. Here's an example of how to create a custom retriever.

```py
class CustomRetriever(BaseRetriever):
    def retrieve(self, query: str) -> dict:
        # Implement your custom retrieval logic here
        # This method should return a model response based on the query
        pass

    def get_context(self, query: str):
        # Implement your custom context retrieval logic here
        # This method should return relevant context based on the query
        pass
```

**2. Customizing Retrieval Logic**: Users can customize the retrieval logic by implementing the retrieve and get_context methods in their custom retriever class. These methods should contain the specific logic for retrieving model responses and context information based on the user's query.

**3. Custom Configuration data model**: Users can also provide the data model for the configurations which will be specific to their custom retriever class. create a new custom retriever config model class that extends the base retriever config model class and specify the configuration fields and their types.

```py
class CustomRetrieverConfigModel(BaseRetrieverConfigModel):
    custom_field: str = "default_value"
```

**4. Custom Configuration**: If you are creating a custom retriever config model which contains specific configurations for the custom retriever component, then you also need a custom configuration class that extends BaseRetrieverConfig to define their own configuration class specific to their custom retriever component. For example:

```py
class CustomRetrieverConfig(BaseRetrieverConfig):
    data_model = CustomRetrieverConfigModel
```

**5. Using Custom Configuration**: To use the custom configuration class, users can modify their custom retriever class to specify the custom configuration class

```py
class CustomRetriever(BaseRetriever):
    config_class = CustomRetrieverConfig

    def retrieve(self, query: str) -> dict:
        # Implement retrieval logic using custom configuration options
        pass
```

**6. Accessing Base Functionality**: Users can access the functionality provided by the base retriever component, such as getting prompts and chat history, by calling the get_prompt and get_chat_history methods from within their custom retriever class. User can also override these functionality.
