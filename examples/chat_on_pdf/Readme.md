## Chat with a pdf

**Note:** Edit the pdf path in the etl.json file and openai key in model.json

1. Run etl

    ```bash
    llmstack etl --config_file chat_on_pdf/etl.json
    ```

2. Run model
    ```bash
    llmstack start --config_file chat_on_pdf/model.json
    ```
