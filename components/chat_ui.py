import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def display_chat(model):
    """Handles chat UI and interaction."""
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    user_input = st.text_input("Type your message:", "", key="user_input")

    chat_history = [SystemMessage(content="You are a knowledgeable AI assistant.")]

    if st.button("Send") and user_input:
        chat_history.append(HumanMessage(content=user_input))
        response = model.invoke(chat_history)
        chat_history.append(AIMessage(content=response.content))

        for msg in chat_history:
            if isinstance(msg, HumanMessage):
                st.markdown(f"<div class='user-message'><strong>You:</strong> {msg.content}</div>", unsafe_allow_html=True)
            elif isinstance(msg, AIMessage):
                st.markdown(f"<div class='ai-message'><strong>AI:</strong> {msg.content}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
