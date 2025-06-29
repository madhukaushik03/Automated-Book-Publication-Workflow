# rl_train_agent.py

from sentence_transformers import SentenceTransformer
from rl_agent_model import RLAgent
import numpy as np

# Simulated document versions (replace with real ones later)
documents = [
    "Modern rewrite of Chapter 1 with simple vocabulary.",
    "Edited version with formal grammar.",
    "AI-reviewed version with poetic tone.",
    "Original text with classical style."
]

# Simulated user preferences (index of best version per query)
# Later, you will replace this with real-time user feedback
preferences = {
    "modern version": 0,
    "grammatical correctness": 1,
    "poetic expression": 2,
    "authenticity": 3
}

# Initialize embedding model and RL agent
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(documents)
agent = RLAgent(input_size=embeddings.shape[1], num_actions=len(documents))

# Training loop
epochs = 20
for epoch in range(epochs):
    print(f"\n📚 Epoch {epoch+1}/{epochs}")

    for query, correct_index in preferences.items():
        print(f"🔍 Query: {query}")

        # Encode the query
        query_embedding = model.encode([query])[0]

        # Simulate RL agent picking an action (document index)
        action = agent.select_action(query_embedding)
        print(f"🤖 Agent picked index: {action} | Correct: {correct_index}")

        # Reward: 1 if correct, else 0
        reward = 1 if action == correct_index else 0

        # Simulate environment transition (same query next step here)
        next_embedding = model.encode([query])[0]

        # Train agent
        agent.train_step(query_embedding, action, reward, next_embedding)

print("\n✅ Training complete. You can now use the trained agent in rl_search.py.")

