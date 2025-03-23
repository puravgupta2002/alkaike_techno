import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def extract_topics(news_list):
    all_topics = []

    for news in news_list:
        doc = nlp(news["Summary"])
        topics = [chunk.text for chunk in doc.noun_chunks]
        all_topics.extend(topics)

    topic_counts = Counter(all_topics)
    common_topics = [topic for topic, count in topic_counts.items() if count > 1]
    unique_topics = [topic for topic, count in topic_counts.items() if count == 1]

    return {"Common Topics": common_topics, "Unique Topics": unique_topics}
