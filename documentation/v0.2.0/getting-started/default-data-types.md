# 📘 Default Data Types

By default, the LLM stack supports the following data types:

### CSV

To use CSV as a source, use the data type (the first argument to the `add_source()` method) as `csv`. Eg:&#x20;

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
 fields={"openai_api_key": "Paste your Open AI key"}
)
model.add_source("csv", "valid_csv_path_or_url")
```

### PDF

To use pdf as a source, use the data type as `pdf`. Eg:

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
 fields={"openai_api_key": "Paste your Open AI key"}
)
model.add_source("pdf", "valid_pdf_path_or_url")
```

### Web

To use the web as a source, use the data type as `web`. Eg:

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
 fields={"openai_api_key": "Paste your Open AI key"}
)
model.add_source("web", "valid_web_url")
```

### JSON

To use JSON as a source, use the data type as `json`. Eg:

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
 fields={"openai_api_key": "Paste your Open AI key"}
)
model.add_source("json", "valid_json_path_or_url")
```

### Markdown

To use markdown as a source, use the data type as `markdown`. Eg:

```python
from genai_stack.model import OpenAIGpt35Model

model = OpenAIGpt35Model.from_kwargs(
 fields={"openai_api_key": "Paste your Open AI key"}
)
model.add_source("markdown", "valid_markdown_path_or_url")
```

To make predictions you can execute the below code snippet:

```python
response = model.predict("<Question on top of any of your data>")
print(response)
```
