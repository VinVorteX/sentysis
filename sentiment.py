# sentiment.py
from textblob import TextBlob

def sentiment(text, stop_words):
    blob = TextBlob(text)
    filtered_text = ' '.join([w for w in blob.words if w not in stop_words])
    filtered_blob = TextBlob(filtered_text)
    sentiment_score = filtered_blob.sentiment.polarity
    return sentiment_score
