# 📖 Advanced Usage

**Template Customization:** The system allows seamless modification of prompt templates tailored for distinct use cases. The templates are of the type `PromptTemplate` which can be imported from the `langchain` module.

- **Simple Chat Prompt Template (`simple_chat_prompt_template`):** Template for straightforward conversational prompts. The simple_chat_prompt_template should have a single {query} and {history} placeholders.
- **Contextual Chat Prompt Template (`contextual_chat_prompt_template`):** Template catering to prompts within a specific context. The contextual_chat_prompt_template should have a single {query}, {history}, and {context} placeholders.
- **Contextual QA Prompt Template (`contextual_qa_prompt_template`):** Templates designed for prompts related to contextual questions and answers. The contextual_qa_prompt_template should have a single {query} and {context} placeholders.
- **Validation Prompt Template (`validation_prompt_template`):** Templates utilized to validate prompts. The validation_prompt_template should have a single {text}  and {format_instructions} placeholder.

Example:

```python
from langchain import PromptTemplate
from genai_stack.prompt_engine.engine import PromptEngine

conversational_prompt_with_context_template = """
The following is a conversation between human and AI. Use the following pieces of context to complete the
conversation. If AI don't know the answer, AI will say that it doesn't know, don't try to make up an answer.
AI will provide an answer which is factually correct and based on the information given in the context.
AI will mention any quotes supporting the answer if it's present in the context.

CONTEXT: {context}

CURRENT CONVERSATIONS:
{history}
HUMAN: {query}
AI:
"""

CONVERSATIONAL_PROMPT_WITH_CONTEXT = PromptTemplate(
    template=conversational_prompt_with_context_template,
    input_variables=["context", "history", "query"]
)

prompt_engine = PromptEngine.from_kwargs(
    simple_chat_prompt_template=CONVERSATIONAL_PROMPT_WITH_CONTEXT
)
```

**Validation Control:** The "should_validate" parameter can be adjusted based on the requirement.

- If set to 'true', the user query undergoes validation to ensure safety, and the template is returned.

- If set to 'false', the user query bypasses the validation process, and a value error is thrown.


Example:

```python
prompt_engine = PromptEngine.from_kwargs(should_validate=False)
```



### API References:


### `validate_prompt()`

**Input:**
- `text`: String

**Output:**

```
{
  decision: Boolean
  reason: String
  response: String
}
```

### `get_prompt_template()`

**Input:**
- `promptType`: PromptTypeEnum
- `Query`: String

**Output:**
- `PromptTemplate`
