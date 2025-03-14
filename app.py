import streamlit as st
from models.huggingface_model import initialize_llm
from models.openai_model import initialize_chat_openai
from components.chat_ui import display_chat
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="wide")

st.sidebar.header("⚙️ Model Selection")
model_choice = st.sidebar.radio("Choose a Model", ["OpenAI", "Hugging Face"], index=0)

if model_choice == "Hugging Face":
    hf_api_token = os.getenv("HF_API_TOKEN")
    model = initialize_llm(hf_api_token)
else:
    model = initialize_chat_openai()

display_chat(model)
