from google import genai

from cred import gemini_api_key


# Creating client with gemini
client = genai.Client(api_key = gemini_api_key) 