from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

def initialize_llm(api_token: str):
    """Initializes the Hugging Face LLM endpoint."""
    llm = HuggingFaceEndpoint(
        repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        huggingfacehub_api_token=api_token
    )
    return ChatHuggingFace(llm=llm)
