import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HUGGINGFACE_MODEL_URL = os.getenv("HUGGINGFACE_MODEL_URL")

def generate_image(prompt):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt
    }
    response = requests.post(HUGGINGFACE_MODEL_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        print("Hata:", response.text)
        return None
    
    return response.content
