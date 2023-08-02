import streamlit as st
from app.services import get_chat_history

st.title("LLM Stack chatbot")

chat_history = get_chat_history()
print(chat_history)
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
