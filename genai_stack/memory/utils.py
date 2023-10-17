from typing import List

def parse_chat_conversation_history(response:list) -> str:
    history = ""
    for i in range(len(response)):
        if i%2 == 0:
            history+=f"HUMAN : {response[i].content}\n"
        else:
            history+=f"YOU : {response[i].content}\n"
            
    return history

def parse_vectordb_chat_conversations(
        search_results: List[str]
    ) -> str:
    history = ""
    for document in search_results:
        history+=document+"\n"
    return history   

def extract_text(key:str, text:str) -> str:
    text_list = text.splitlines()
    if key == "user":
        return text_list[0].replace('input: ','')
    elif key == "model":
        return text_list[1].replace('output: ','')
    

def create_kwarg_map(config:dict) -> dict:
    """Creates and returns the kwarg_map."""
    index_name = config.index_name
    kwarg_map = {
        "ChromaDB":{
            "index_name":index_name
        },
        "Weaviate":{
            "index_name":index_name.capitalize(),
            "text_key":f"{index_name}_key"
        }
    }
    return kwarg_map
