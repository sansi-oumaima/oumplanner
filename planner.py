import os
import requests

API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN") or ""  # sera injecté par Streamlit Cloud
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

def query_huggingface(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

def generate_trip(user_question: str) -> str:
    payload = {
        "inputs": {
            "past_user_inputs": [],
            "generated_responses": [],
            "text": user_question
        }
    }
    result = query_huggingface(payload)
    if isinstance(result, dict) and "error" in result:
        return f"Erreur API : {result['error']}"
    return result[0]["generated_text"]
