import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")
gemini_api_model = os.getenv("GEMINI_API_MODEL")


if not gemini_api_key or not gemini_base_url or not gemini_api_model:
    print("please load following things gemini_api_key, gemini_base_url, gemini_api_model")
    exit(1)

class Secret:
    def __init__(self):
        self.gemini_api_key = gemini_api_key
        self.gemini_base_url = gemini_base_url
        self.gemini_api_model = gemini_api_model
