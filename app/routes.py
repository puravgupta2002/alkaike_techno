from fastapi import APIRouter
from app.scraper import fetch_tesla_news
from app.sentiment import analyze_sentiment
from app.topic_extraction import extract_topics

router = APIRouter()

@router.get("/results")
def get_results():
    news_data = fetch_tesla_news()
    sentiment_results = analyze_sentiment(news_data)
    topics = extract_topics(news_data)

    output_data = {
        "Extracted News Articles": news_data,
        "Sentiment Analysis Results": sentiment_results,
        "Common Topics": topics["Common Topics"],
        "Unique Topics": topics["Unique Topics"],
        "Most Positive/Negative News Article": max(sentiment_results, key=lambda x: x["Score"])
    }

    return output_data

