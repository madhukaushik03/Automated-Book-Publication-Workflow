# rl_search.py

from sentence_transformers import SentenceTransformer
from rl_agent_model import RLAgent
import numpy as np
import json

# Step 1: Document Versions
documents = [
    "Modern rewrite of Chapter 1 with simple vocabulary.",
    "Edited version with formal grammar.",
    "AI-reviewed version with poetic tone.",
    "Original text with classical style."
]

sources = ["ai_writer", "human_editor", "ai_reviewer", "original"]

# Step 2: Initialize model and agent
model = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = model.encode(documents)
agent = RLAgent(input_size=doc_embeddings.shape[1], num_actions=len(documents))
agent.load("trained_rl_agent.pth")  # ✅ Add this line to load trained model
agent.epsilon = 0.0

# Step 3: Accept user query
query = input("🔍 Enter your search query: ")
query_embedding = model.encode([query])[0]

# Step 4: Agent selects best document
selected_index = agent.select_action(query_embedding)
selected_version = documents[selected_index]

# Step 5: Show all documents
print("\n📚 Top versions:")
for idx, (doc, src) in enumerate(zip(documents, sources)):
    print(f"\n{idx+1}. 📄 Source: `{src}`")
    print("-" * 80)
    print(doc[:300] + ("..." if len(doc) > 300 else ""))
    print("=" * 80)

# Step 6: Show agent recommendation
print(f"\n🤖 RL Agent recommends version by `{sources[selected_index]}`")

# Step 7: Get user feedback
feedback = input("✅ Which result did you find most relevant? (Enter index 0–3 or 'n' to skip): ")

# Step 8: Log feedback if valid
if feedback.isdigit() and 0 <= int(feedback) < len(documents):
    feedback_index = int(feedback)
    reward = 1.0 if feedback_index == selected_index else 0.0

    # Log episode for RL training
    with open("rl_logs.jsonl", "a") as f:
        episode = {
            "query": query,
            "chosen_index": selected_index,
            "recommended_source": sources[selected_index],
            "feedback_index": feedback_index,
            "reward": reward,
            "sources": sources,
        }
        f.write(json.dumps(episode) + "\n")

    print(f"📈 Feedback logged. Reward: {reward}")
else:
    print("⏩ Skipped feedback.")
