# 🗒 Without Vector Store

#### Running the model in terminal with a http server

Follow these steps to set up and run the Language Model (LLM) Stack using an HTTP server:

**Step 1: Starting the LLM Model**

Open your terminal and run the following command to start the LLM model using the llmstack package:

````
```bash
llmstack start --config_file llm_stack_config.json
```
````

Once started, you will see a response that includes a visual representation of the service's startup progress. It will also show the address where the server is running (e.g., [http://127.0.0.1:8082](http://127.0.0.1:8082/)).

Now you should see a response like below.

````
```bash
██╗     ██╗     ███╗   ███╗    ███████╗████████╗ █████╗  ██████╗██╗  ██╗
██║     ██║     ████╗ ████║    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██║     ██║     ██╔████╔██║    ███████╗   ██║   ███████║██║     █████╔╝
██║     ██║     ██║╚██╔╝██║    ╚════██║   ██║   ██╔══██║██║     ██╔═██╗
███████╗███████╗██║ ╚═╝ ██║    ███████║   ██║   ██║  ██║╚██████╗██║  ██╗
╚══════╝╚══════╝╚═╝     ╚═╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

Failed to get VectorDB
Failed to get Retriever
INFO:     Started server process [641734]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8082 (Press CTRL+C to quit)
```
````

**Step 2: Testing the Model via Python Script**

In a separate terminal or code editor, use the following Python script to test the LLM model by making an HTTP request to its predict endpoint:

```
import requests
response = requests.post("http://localhost:8082/predict/",data="Python program to add two numbers.")
print(response.text)
```

This script sends a text input to the model and prints the response from the model.
