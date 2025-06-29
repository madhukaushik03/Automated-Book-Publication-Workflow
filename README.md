# Automated Book Publication Workflow

An AI-enhanced system that transforms traditional book chapters with the help of LLMs, supports human editing, stores multiple versions using ChromaDB, and uses Reinforcement Learning to intelligently retrieve the best version based on user feedback.

## Features
 
🕸️ Web Scraping & Screenshots (via Playwright)

✍️ AI-Based Spinning (LLM-generated rewrites)

👩‍💼 Human-in-the-Loop Editing via Streamlit UI

🧠 RL-Based Intelligent Retrieval (PyTorch + custom DQN)

📦 Version Control with ChromaDB

📈 Continuous Learning via Feedback

## 🗂️ Folder Structure

├── ai_writer.py             # AI-based rewriting

├── reviewer.py              # Review version using LLM

├── editor.py                # (Optional) Edit logic

├── workflow_ui.py           # Streamlit interface

├── scraper.py               # Web scraping and screenshots

├── chroma_store.py          # Store/retrieve to/from ChromaDB

├── rl_search.py             # RL-powered intelligent search

├── rl_agent_model.py        # DQN-based RL agent (PyTorch)

├── train_from_logs.py       # Train RL agent from logs

├── rl_logs.jsonl            # Feedback log

├── trained_rl_agent.pth     # Saved RL model

├── requirements.txt         # Python dependencies

└── README.md                # Project doc

## ⚙️ Setup Instructions

git clone https://github.com/madhukaushik03/Automated-Book-Publication-Workflow.git

cd Automated-Book-Publication-Workflow

python -m venv venv

venv\Scripts\activate   # On Windows

source venv/bin/activate   # On Linux/macOS

pip install -r requirements.txt

## 🚀 How to Use

Scrape chapter content:
python scraper.py

Spin chapter with AI:
python ai_writer.py

Review it with LLM:
python reviewer.py

Open UI for Human-in-the-Loop Workflow:
streamlit run workflow_ui.py

Use RL agent for intelligent search:
python rl_search.py

Retrain RL agent from feedback logs:
python train_from_logs.py

## 🧠 RL Agent Training

Agent is based on Deep Q-Network (DQN) trained on user preference logs (rl_logs.jsonl).

Action: version index | State: query embedding | Reward: match with user-selected version.

Model: trained_rl_agent.pth

## 🎯 Future Scope

Convert Writer/Reviewer into agentic API services

Expand to more books/chapters

Integrate with full publishing platforms

## 👩‍💻 Developed by

Madhu Kaushik – AI Enthusiast & Developer

