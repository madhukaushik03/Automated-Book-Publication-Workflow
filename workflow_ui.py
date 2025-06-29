# import streamlit as st
# import os
# import requests
# from dotenv import load_dotenv
# import chromadb

# # Load Gemini API key
# load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")
# GEMINI_URL = (
#     "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
# )
# HEADERS = {"Content-Type": "application/json"}
# PARAMS = {"key": API_KEY}

# # Paths
# SPUN_PATH = "chapter1_spun_by_ai.txt"
# EDITED_PATH = "chapter1_human_edited.txt"
# REVIEWED_PATH = "chapter1_final_reviewed.txt"

# def load_text(path):
#     if os.path.exists(path):
#         with open(path, "r", encoding="utf-8") as f:
#             return f.read()
#     return ""

# def save_text(path, text):
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(text)

# def call_gemini(prompt):
#     payload = {"contents": [{"parts": [{"text": prompt}]}]}
#     resp = requests.post(GEMINI_URL, params=PARAMS, headers=HEADERS, json=payload)
#     if resp.status_code == 200:
#         return resp.json()["candidates"][0]["content"]["parts"][0]["text"]
#     return f"[API ERROR {resp.status_code}]"

# # ------------------ Streamlit UI ------------------

# st.title("📖 Human-in-the-Loop Chapter Refinement")

# # Initialize session state
# if "current_text" not in st.session_state:
#     st.session_state.current_text = load_text(EDITED_PATH) or load_text(SPUN_PATH)

# st.subheader("✍️ Edit or Review Chapter")
# edited_text = st.text_area("Your current draft:", value=st.session_state.current_text, height=400)

# col1, col2, col3 = st.columns(3)

# # AI Review
# if col1.button("🧠 AI Review This"):
#     prompt = f"""Improve the following chapter for clarity, grammar, tone, and fluency. Only return the revised chapter:\n\n{edited_text}"""
#     ai_output = call_gemini(prompt)
#     st.session_state.current_text = ai_output.strip()
#     save_text(EDITED_PATH, st.session_state.current_text)
#     st.success("✅ AI reviewed version is now editable again!")

# # Save without review
# if col2.button("💾 Save As-Is"):
#     st.session_state.current_text = edited_text
#     save_text(EDITED_PATH, edited_text)
#     st.info("✍️ Version saved. You can still continue editing or review again.")

# # Finalize
# if col3.button("✅ Finalize Chapter"):
#     save_text(REVIEWED_PATH, st.session_state.current_text)
#     st.success(f"🎉 Final version saved as '{REVIEWED_PATH}'")
#     st.balloons()

# st.caption("🔁 You can edit → review → edit → review repeatedly before finalizing.")




# # Load ChromaDB and Collection
# client = chromadb.PersistentClient(path="./chroma_storage")
# collection = client.get_or_create_collection(name="book_versions")

# st.markdown("---")
# with st.expander("📚 View All Saved Versions"):
#     try:
#         results = collection.get(include=["documents", "metadatas"])
#         for doc, meta in zip(results["documents"], results["metadatas"]):
#             st.markdown(f"#### 📄 Source: `{meta['source']}`")
#             st.code(doc[:1000] + ("..." if len(doc) > 1000 else ""), language="text")
#     except Exception as e:
#         st.error(f"Failed to load versions: {e}")

import streamlit as st
import os
import requests
from dotenv import load_dotenv
import chromadb

# Load Gemini API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
)
HEADERS = {"Content-Type": "application/json"}
PARAMS = {"key": API_KEY}

# Paths
SPUN_PATH = "chapter1_spun_by_ai.txt"
EDITED_PATH = "chapter1_human_edited.txt"
REVIEWED_PATH = "chapter1_final_reviewed.txt"

# Load/Save helpers
def load_text(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def save_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

# Gemini API call
def call_gemini(prompt):
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    resp = requests.post(GEMINI_URL, params=PARAMS, headers=HEADERS, json=payload)
    if resp.status_code == 200:
        return resp.json()["candidates"][0]["content"]["parts"][0]["text"]
    return f"[API ERROR {resp.status_code}]"

# ChromaDB Setup
client = chromadb.PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection(name="book_versions")

def add_to_chromadb(version_id, text, source):
    try:
        collection.add(
            documents=[text],
            metadatas=[{"source": source}],
            ids=[version_id]
        )
    except chromadb.errors.IDAlreadyExistsError:
        # Optionally handle ID conflict (e.g., update/delete old first)
        pass

# ------------------ Streamlit UI ------------------

st.title("📖 Human-in-the-Loop Chapter Refinement")

# Initialize session state
if "current_text" not in st.session_state:
    st.session_state.current_text = load_text(EDITED_PATH) or load_text(SPUN_PATH)

st.subheader("✍️ Edit or Review Chapter")
edited_text = st.text_area("Your current draft:", value=st.session_state.current_text, height=400)

col1, col2, col3 = st.columns(3)

# AI Review
if col1.button("🧠 AI Review This"):
    prompt = f"""Improve the following chapter for clarity, grammar, tone, and fluency. Only return the revised chapter:\n\n{edited_text}"""
    ai_output = call_gemini(prompt)
    st.session_state.current_text = ai_output.strip()
    save_text(EDITED_PATH, st.session_state.current_text)
    add_to_chromadb("chapter1_human_edited", st.session_state.current_text, "ai_reviewer")
    st.success("✅ AI reviewed version is now editable again!")

# Save without review
if col2.button("💾 Save As-Is"):
    st.session_state.current_text = edited_text
    save_text(EDITED_PATH, edited_text)
    add_to_chromadb("chapter1_human_edited", edited_text, "human_editor")
    st.info("✍️ Version saved. You can still continue editing or review again.")

# Finalize
if col3.button("✅ Finalize Chapter"):
    save_text(REVIEWED_PATH, st.session_state.current_text)
    add_to_chromadb("chapter1_final_reviewed", st.session_state.current_text, "final_reviewed")
    st.success(f"🎉 Final version saved as '{REVIEWED_PATH}'")
    st.balloons()

st.caption("🔁 You can edit → review → edit → review repeatedly before finalizing.")

# ------------------ View All Stored Versions ------------------

# st.markdown("---")
# with st.expander("📚 View All Saved Versions"):
#     try:
#         results = collection.get(include=["documents", "metadatas"])
#         for doc, meta in zip(results["documents"], results["metadatas"]):
#             st.markdown(f"#### 📄 Source: `{meta['source']}`")
#             st.code(doc[:1000] + ("..." if len(doc) > 1000 else ""), language="text")
#     except Exception as e:
#         st.error(f"Failed to load versions: {e}")
