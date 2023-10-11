from typing import List
from langchain.docstore.document import Document

def parse_chat_conversation_history(response:list) -> str:
    history = ""
    for i in range(len(response)):
        if i%2 == 0:
            history+=f"HUMAN : {response[i].content}\n"
        else:
            history+=f"YOU : {response[i].content}\n"
            
    return history

def parse_chat_conversation_history_search_result(search_results: List[Document]) -> str:
    history = ""
    for document in search_results:
        history+=f"{document.page_content.replace('input','HUMAN').replace('output','YOU')}\n"
    return history  

def extract_text(key:str, text:str) -> str:
    text_list = text.splitlines()
    if key == "user":
        return text_list[0].replace('input: ','')
    elif key == "model":
        return text_list[1].replace('output: ','')
    

def format_index_name(config:dict) -> dict:
    """Formats index name and returns the kwarg_map."""
    index_name = config.index_name.capitalize()
    kwarg_map = {
        "ChromaDB":{
            "index_name":index_name
        },
        "Weaviate":{
            "index_name":index_name,
            "test_key":f"{index_name.lower()}_key"
        }
    }
    return kwarg_map, index_name
