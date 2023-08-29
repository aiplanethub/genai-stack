## Chat with a pdf

**Note:** Edit the pdf path in the etl.json file and openai key in model.json

1. Run etl

    ```bash
    genai-stack etl --config_file etl.json
    ```

2. Run model
    ```bash
    genai-stack start --config_file model.json
    ```
