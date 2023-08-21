import streamlit as st
from services import get_chat_history, get_response

st.title("GenAI Stack chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = get_chat_history()

if "source_documents" not in st.session_state:
    st.session_state.source_documents = [
        {"content": "No source documents here. Ask a question to get the source documents.", "metadata": {}}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input():
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response["result"])

    st.session_state.source_documents = response["source_documents"]
    with st.sidebar:
        st.title("Source Documents")
        for idx, document in enumerate(st.session_state.source_documents):
            st.markdown(f"**Document {idx + 1}** \n" + document["content"])
            st.markdown(f"**Metadata:**")
            st.markdown(document["metadata"])
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
