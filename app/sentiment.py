from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze_sentiment(news_list):
    batch_size = 2
    predictions = []

    for i in range(0, len(news_list), batch_size):
        batch = [news["Summary"] for news in news_list[i: i + batch_size]]
        results = classifier(batch)

        for news, result in zip(news_list[i: i + batch_size], results):
            predictions.append({
                "Title": news["Title"],
                "Summary": news["Summary"],
                "Sentiment": result["label"],
                "Score": result["score"]
            })

    return predictions
