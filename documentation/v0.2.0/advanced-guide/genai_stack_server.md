# 💻 Setup GenAI Server

Create a directory where you intend to set up your GenAI Server. Within this directory, add the following files:

- `main.py`: This Python script serves as the entry point for your GenAI Server.
- `server.conf`: This configuration file contains settings related to your database.
- `stack_config.json`: This JSON configuration file defines the components and their configurations for your server stack.


```
your_directory_name/
|-- server.conf
|-- stack_config.json
|-- main.py
```

## Configuration Files

### `server.conf`

Edit the `server.conf` file to specify database-related settings.

```ini
[database]
database_name = db
database_driver = sqlite
```

- `database_name`: Set this to your preferred database name.
- `database_driver`: Specify the database driver to sqlite. Currently, we only support sqlite.

### `stack_config.json`

```json
{
    "components": {
        "vectordb": {
            "name": "weaviate_db",
            "config": {
                "url": "http://localhost:8080/",
                "index_name": "Testing",
                "text_key": "test",
                "attributes": ["page", "path"]
            }
        },
        "memory": {
            "name": "langchain",
            "config": {}
        },
        "llm_cache": {
            "name": "cache",
            "config": {}
        },
        "model": {
            "name": "gpt3.5",
            "config": {
                "parameters": {
                    "openai_api_key": "your_api_key_here"
                }
            }
        },
        "embedding": {
            "name": "langchain",
            "config": {
                "name": "HuggingFaceEmbeddings",
                "fields": {
                    "model_name": "sentence-transformers/all-mpnet-base-v2",
                    "model_kwargs": {"device": "cpu"},
                    "encode_kwargs": {"normalize_embeddings": false}
                }
            }
        },
        "prompt_engine": {
            "name": "engine",
            "config": {
                "should_validate": true
            }
        },
        "retriever": {
            "name": "langchain",
            "config": {}
        }
    }
}
```

Customize the `stack_config.json` file to define the components for your GenAI Server stack.

- Customize the components as needed.

## Running the Server

### `main.py`:
- In `main.py`, you import two functions (`read_configurations` and `get_current_stack`) from the `genai_server` package to initialize your GenAI Server.

- Provide the path to the current folder where your configuration files reside.

- `read_configurations(path)` reads configurations from `server.conf` and `stack_config.json` at the specified path and returns two sets of configurations:

   - `server_configurations`: Specific to your GenAI Server.

   - `stack_configurations`: Default stack configurations from `stack_config.json`, defining the configurations required for the components to work together.

- Pass `stack_configurations` to `get_current_stack(config=stack_configurations)`. This function initializes your GenAI Server's stack based on these configurations. The stack is like a toolkit of components, each with its own settings, ready to serve your AI applications.


```py
from genai_stack.genai_server.settings.config import read_configurations
from genai_stack.genai_server.utils import get_current_stack

path = "path/to/the/directory"

server_configurations, stack_configurations = read_configurations(path)

stack = get_current_stack(config=stack_configurations)

stack.run_server(host="127.0.0.1", port=5000)
```

To start your GenAI Server, use the `main.py` script. Open a terminal and navigate to the directory where `main.py` is located. Then, execute the following command:

```bash
python3 main.py
```

Your GenAI Server is now up and running, ready to serve AI-based applications and services!
