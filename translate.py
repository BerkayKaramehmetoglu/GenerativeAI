import os
import requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_TRANSLATE_API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")

def translate_text(text, target_language="en"):
    url = f"https://translation.googleapis.com/language/translate/v2?key={GOOGLE_TRANSLATE_API_KEY}"
    data = {
        "q": text,
        "source": "tr",
        "target": target_language,
        "format": "text"
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result["data"]["translations"][0]["translatedText"]
