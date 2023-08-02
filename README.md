# LLM Stack

An end to end LLM framework

-   Documentation: https://llm_stack.readthedocs.io.

## Usage

1. Install with pip
    ```bash
    pip install git+https://github.com/aiplanethub/llmstack.git
    ```
2. Verify installation
    ```bash
    llmstack version
    ```
3. Check List of commands
    ```bash
    llmstack --help
    ```

## Running a Model

1.  Run an LLM Model

    ```bash
    llmstack start
    ```

    By default, the `start` command uses **gpt4all** model. You can customize the config json to use other models like GPt3.

2.  Now you should see an http server(uvicorn) running as below

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

3.  Make a request to the [/predict](http://127.0.0.1:8082/predict) endpoint to get response from the LLM.

    ```python
    import requests
    repsonse = requests.post("http://localhost:8082/predict/",data="Python program to add two numbers.")
    print(response.text)
    ```

    ````bash
        # Response from the LLM

        Here is a Python program to add two numbers:

        ```python
        # take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # add the numbers
        sum = num1 + num2

        # print the result
        print("The sum of", num1, "and", num2, "is", sum)
        ```

        In this program, we take two numbers as input from the user using the `input()` function. We convert the input to float using the `float()` function to handle decimal numbers.

        Then, we add the two numbers using the `+` operator and store the result in the variable `sum`.

        Finally, we print the result using the `print()` function.
    ````

## Documentation
Documentation and better usage of the tool can be found in the [./docs/components](https://github.com/aiplanethub/llmstack/tree/main/docs/components) folder of this repo
