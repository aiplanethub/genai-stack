import streamlit as st
from services import get_chat_history

st.title("LLM Stack chatbot")

chat_history = get_chat_history()
# Display chat messages from history on app rerun
for message in chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
