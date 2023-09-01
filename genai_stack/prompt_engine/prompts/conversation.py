from langchain import PromptTemplate

conversational_prompt_template = """
The following is a conversation between you and human. If you don't know the answer, just say that you don't know,
don't try to make up an answer.

CURRENT CONVERSATIONS:
{history}
HUMAN: {query}
YOU:
"""


conversational_prompt_with_context_template = """
The following is a conversation between you and human. Use the following pieces of context to complete the
conversation. If you don't know the answer, just say that you don't know, don't try to make up an answer.
Please provide an answer which is factually correct and based on the information given in the context.
Mention any quotes supporting the answer if it's present in the context.

CONTEXT: {context}

CURRENT CONVERSATIONS:
{history}
HUMAN: {query}
YOU:
"""

CONVERSATIONAL_PROMPT = PromptTemplate(
    template=conversational_prompt_template,
    input_variables=["history", "query"]
)
CONVERSATIONAL_PROMPT_WITH_CONTEXT = PromptTemplate(
    template=conversational_prompt_with_context_template,
    input_variables=["context", "history", "query"]
)
