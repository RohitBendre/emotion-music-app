import requests
import os

API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"

headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
}

def analyze_emotion(text: str) -> str:
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    result = response.json()

    if isinstance(result, list):
        return result[0][0]["label"].lower()
    return "neutral"