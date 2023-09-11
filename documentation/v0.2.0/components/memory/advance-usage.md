# 📖 Advanced Usage

## Create your own Custom Memory Component

Each stack component has three Base Interfaces.

Base Interfaces for the Memory component

```py
class BaseMemoryConfigModel(BaseModel):
    """
    Data Model for the configs
    """
    pass


class BaseMemoryConfig(StackComponentConfig):
    data_model = BaseMemoryConfigModel


class BaseMemory(StackComponent):

    def get_user_text(self) -> str:
        """
        This method returns the user query
        """
        raise NotImplementedError()

    def get_model_text(self) -> str:
        """
        This method returns the model response
        """
        raise NotImplementedError()

    def get_text(self) -> dict:
        """
        This method returns both user query and model response
        """
        raise NotImplementedError()

    def add_text(self, user_text:str, model_text:str) -> None:
        """
        This method stores both user query and model response
        """
        raise NotImplementedError()

    def get_chat_history(self) -> str:
        """
        This method returns the chat conversation history
        """
        raise NotImplementedError()
```

**1. Creating a Custom Memory Component**: Create a new class that extends the BaseMemory class. Here's an example of how to create a custom memory.

```py
class CustomMemory(BaseMemory):
    def get_user_text(self) -> str:
        # Implement logic to retrieve user's query
        pass

    def get_model_text(self) -> str:
        # Implement logic to retrieve model's response
        pass

    def get_text(self) -> dict:
        # Implement logic to return both user's query and model's response
        pass

    def add_text(self, user_text: str, model_text: str) -> None:
        # Implement logic to store user's query and model's response
        pass

    def get_chat_history(self) -> str:
        # Implement logic to retrieve chat conversation history
        pass
```

**2. Customizing Memory Logic**: In the CustomMemory class, users need to implement the methods defined in the BaseMemory interface. These methods include:

-   get_user_text(): Implement this method to retrieve the user's query.
-   get_model_text(): Implement this method to retrieve the model's response.
-   get_text(): Implement this method to return both the user's query and the model's response, typically as a dictionary or a structured data format.
-   add_text(user_text, model_text): Implement this method to store both the user's query and the model's response in your custom memory component.
-   get_chat_history(): Implement this method to retrieve the complete chat conversation history.

**3. Custom Configuration data model**: Users can also provide the data model for the configurations which will be specific to their custom memory class. create a new custom memory config model class that extends the base memory config model class and specify the configuration fields and their types.

```py
class CustomMemoryConfigModel(BaseMemoryConfigModel):
    custom_field: str = "default_value"
```

**4. Custom Configuration**: If you are creating a custom memory config model which contains specific configurations for the custom memory component, then you also need a custom configuration class that extends BaseMemoryConfig to define their own configuration class specific to their custom memory component. For example:

```py
class CustomMemoryConfig(BaseMemoryConfig):
    data_model = CustomMemoryConfigModel
```

**5. Using Custom Configuration**: To use the custom configuration class, users can modify their custom memory class to specify the custom configuration class

```py
class CustomMemory(BaseMemory):
    config_class = CustomMemoryConfig
```
