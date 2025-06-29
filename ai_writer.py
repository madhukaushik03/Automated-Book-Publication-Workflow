

import os
import requests
import json
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Read chapter text
with open("chapter1_raw.txt", "r", encoding="utf-8") as f:
    original_text = f.read()

# Gemini endpoint
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# JSON payload for API
payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": f"""Rewrite (spin) this chapter in modern style but preserve the meaning:

{original_text}
"""
                }
            ]
        }
    ]
}

# Send POST request to Gemini API
response = requests.post(url, headers={"Content-Type": "application/json"}, json=payload)

# Parse result
if response.status_code == 200:
    result = response.json()
    ai_output = result['candidates'][0]['content']['parts'][0]['text']

    # Save to file
    with open("chapter1_spun_by_ai.txt", "w", encoding="utf-8") as f:
        f.write(ai_output)

    print(" AI-spun chapter saved to chapter1_spun_by_ai.txt")

else:
    print(" Error:", response.status_code, response.text)
