#  Automated Book Publication Workflow – AI-Powered Chapter Editor

An AI-powered pipeline to automate book publication using web scraping, content generation with Gemini API, human-in-the-loop editing, and ChromaDB-based versioning and intelligent retrieval.


## Features

-  **Web Scraping & Screenshot** – Scrapes content from [Wikisource](https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1)
-  **AI Chapter Spinning** – Uses Google Gemini to rewrite the chapter
-  **Human-in-the-Loop Iteration** – Optional editing/review phase before finalizing
-  **Final Review with AI** – Polishes the rewritten content
-  **ChromaDB Vector Storage** – Stores all versions with metadata
-  **RL-style Retrieval** – Search and retrieve content intelligently using semantic queries
-  **Free API & Tools Used** – Only open-source tools and Gemini (free tier)


##  Tech Stack

| Layer          | Tool/Library                     |
|----------------|----------------------------------|
| Language       | Python                           |
| Web Scraping   | Playwright                       |
| AI Writing     | Gemini 1.5 Flash API (Free)      |
| Vector DB      | ChromaDB                         |
| Screenshot     | Playwright                       |
| Semantic Search| Chroma with MiniLM Embeddings    |


## Project Structure

book_ai_project/
├── ai_writer.py
├── chroma_store.py
├── chroma_query.py
├── scraper.py
├── editor.py
├── reviewer.py
├── chapter1_raw.txt
├── chapter1_spun_by_ai.txt
├── chapter1_final_reviewed.txt
├── chapter1_screenshot.png
└── chroma_storage/ (auto-created)

##  Setup Instructions

1. **Install dependencies**

pip install -r requirements.txt
Set up your .env file

GEMINI_API_KEY=your_api_key_here
Run full pipeline

python scraper.py            # Step 1: Scrape and screenshot
python ai_writer.py          # Step 2: AI "spin" the chapter
python editor.py             # Step 3: (Optional) Human editor
python reviewer.py           # Step 4: AI reviewer finalizes
python chroma_store.py       # Step 5: Save all versions in ChromaDB
python chroma_query.py       # Step 6: Search content by meaning

Run chroma_store.py to regenerate the ChromaDB locally.

## Learning Outcomes
Built full AI content generation pipeline

Integrated free LLM API (Gemini)

Worked with semantic search and vector DB

Applied human-AI collaboration principles

## Contribution & License
This project is for educational purposes only. All rights to source content remain with the original authors.
No commercial use intended.
