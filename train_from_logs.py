# train_from_logs.py

import json
from sentence_transformers import SentenceTransformer
from rl_agent_model import RLAgent
import numpy as np

# Load logs
log_file = "rl_logs.jsonl"
with open(log_file, "r") as f:
    episodes = [json.loads(line) for line in f]

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Get doc versions again (same order as during search)
documents = [
    "Modern rewrite of Chapter 1 with simple vocabulary.",
    "Edited version with formal grammar.",
    "AI-reviewed version with poetic tone.",
    "Original text with classical style."
]
doc_embeddings = model.encode(documents)

# Initialize RL Agent
agent = RLAgent(input_size=doc_embeddings.shape[1], num_actions=len(documents))

# Train on each episode
for ep in episodes:
    query_embedding = model.encode([ep["query"]])[0]
    action = ep["chosen_index"]
    reward = ep["reward"]
    # For simplicity, use same query as next state
    next_embedding = query_embedding
    agent.train_step(query_embedding, action, reward, next_embedding)

print("✅ RL Agent training complete from logs.")
# Save the trained model
agent.save("trained_rl_agent.pth")
print(" Agent saved to trained_rl_agent.pth")