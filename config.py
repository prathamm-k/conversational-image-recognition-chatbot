import os
from dotenv import load_dotenv

load_dotenv()
replicate_api_key = "r8_7ZMqX4RA3ToHdWowah2x2zwbgCO7BSC4X1YxT"
#replicate_api_key = os.getenv("REPLICATE_API_KEY")
print(replicate_api_key)

class Config:
    PAGE_TITLE = "Belirix"

    OLLAMA_MODELS = ('llava:13b', 'llava:34b', 'bakllava')

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                    open-source vision models {OLLAMA_MODELS}.
                    You can can answer questions about images."""
    