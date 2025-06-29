import chromadb
import os
from datetime import datetime

# Persistent ChromaDB client
client = chromadb.PersistentClient(path="./chroma_storage")
collection = client.get_or_create_collection(name="book_versions")

# Helper to add a version
def add_version(version_id, text, source):
    collection.add(
        documents=[text],
        metadatas=[{"source": source}],
        ids=[version_id]
    )
    print(f"✅ Added: {version_id} ({source})")

# Define versioned file naming pattern
files = [
    ("chapter1_raw.txt", "original"),
    ("chapter1_spun_by_ai.txt", "ai_writer"),
    ("chapter1_final_reviewed.txt", "ai_reviewer")
]

# Dynamically include *all* human-edited versions
for fname in os.listdir():
    if fname.startswith("chapter1_human_edited") and fname.endswith(".txt"):
        files.append((fname, "human_editor"))
    elif fname.startswith("chapter1_ai_reviewed_") and fname.endswith(".txt"):
        files.append((fname, "ai_reviewer_looped"))

# Store all
for fname, source in files:
    if os.path.exists(fname):
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        version_id = fname  # Using filename as ID
        add_version(version_id, content, source)
