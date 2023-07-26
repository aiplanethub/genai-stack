from langchain import PromptTemplate

template = """
Context:
{context}

Based on the information provided in Context, please answer the following Prompt:

Prompt:
{user_prompt}

Please limit your response to the content available in the provided documents. If the answer cannot be determined or is uncertain based on the information given, please acknowledge that you cannot provide a definitive solution with the available data.
Your objective is to be as accurate as possible while strictly adhering to the content within the three documents and avoiding the generation of information not explicitly present in them.
"""

BASIC_QA = PromptTemplate.from_template(template)
