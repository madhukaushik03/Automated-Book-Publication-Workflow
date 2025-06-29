

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Load the human-edited (or AI) version
if os.path.exists("chapter1_human_edited.txt"):
    with open("chapter1_human_edited.txt", "r", encoding="utf-8") as f:
        input_text = f.read()
else:
    with open("chapter1_spun_by_ai.txt", "r", encoding="utf-8") as f:
        input_text = f.read()

# Reviewer Prompt
prompt = f"""You're an expert book editor. Review this chapter, fix inconsistencies, improve style, make it more engaging and keep it human-like:

{input_text}
"""

# Prepare payload
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
payload = {
    "contents": [
        {
            "parts": [{"text": prompt}]
        }
    ]
}
headers = {"Content-Type": "application/json"}

# Call Gemini
response = requests.post(url, headers=headers, json=payload)

# Save final version
if response.status_code == 200:
    final_output = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    with open("chapter1_final_reviewed.txt", "w", encoding="utf-8") as f:
        f.write(final_output)
    print("Final reviewed version saved as 'chapter1_final_reviewed.txt'")
else:
    print(" Error:", response.status_code, response.text)
