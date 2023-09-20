from typing import List
from langchain.docstore.document import Document

def parse_search_results(search_results: List[Document]):
    """
    This method returns a content extracted from the documents list.
    """
    result = ""

    for idx, search_result in enumerate(search_results):
        result += f"{idx + 1}. {search_result.page_content} \n"

    return result