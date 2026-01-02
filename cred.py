import os
from dotenv import load_dotenv

# Loading Gemini API key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY", "")

if not gemini_api_key: 
    raise EnvironmentError("Google_gemini_key is not found.")