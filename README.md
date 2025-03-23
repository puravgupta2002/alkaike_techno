# alkaike_techno
# Tesla News Sentiment Analysis

This project scrapes Tesla news articles from BBC, performs sentiment analysis, and extracts key topics.  
It provides a FastAPI backend and a Gradio-based UI.

## Features
- Web scraping of Tesla-related news.
- Sentiment analysis using Hugging Face transformers.
- Named entity recognition (NER) and topic extraction.
- API endpoints for accessing data.
- Interactive Gradio interface.

## Installation
```bash
git clone <repo-url>
cd tesla-news-sentiment-analysis
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
