from typing import List, Optional
from langchain.schema import Document

def parse_chat_conversation_history(response:list) -> str:
    history = ""
    for i in range(len(response)):
        if i%2 == 0:
            history+=f"HUMAN : {response[i].content}\n"
        else:
            history+=f"YOU : {response[i].content}\n"
            
    return history

def parse_vectordb_chat_conversations(
        search_results:List[Document],
        k:int
    ) -> str:
    history = ""
    for document in search_results[-k:]:
        history+=document.page_content+"\n"
    return history   

def extract_text(conversation:List[Document],key:Optional[str] = None) -> str:
    text = conversation[0].page_content
    text_list = text.splitlines()
    user_text = text_list[0].replace('HUMAN: ','')
    model_text = text_list[1].replace('YOU: ','')

    if key == 'user_text':
        return user_text
    elif key == 'model_text':
        return model_text
    else:
        return  {"user_text":user_text, "model_text":model_text}
    
    

def create_kwarg_map(config:dict) -> dict:
    """Creates and returns the kwarg_map."""
    index_name = config.index_name
    kwarg_map = {
        "ChromaDB":{
            "index_name":index_name
        },
        "Weaviate":{
            "index_name":index_name.capitalize(),
            "text_key":"chat_key",
            "properties":[
                {"name":"chat_key", "dataType":["text"]},
                {"name":"timestamp","dataType":["date"]}
            ],
            "attributes":["chat_key", "timestamp"]
        }
    }
    return kwarg_map

def format_conversation(
    user_text:str, 
    model_text:str
) -> str:
    
    return f"HUMAN: {user_text}\nYOU: {model_text}"

def get_conversation_from_document(document:dict, kwarg_map:dict) -> str:

    if 'documents' in document:
        # document from chroma
        return document.get('documents')[0]
    elif 'properties' in document:
        # document from weaviate
        return document.get('properties').get(kwarg_map.get('Weaviate').get('text_key'))