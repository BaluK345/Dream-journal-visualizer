import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def analyze_dream(text):
    doc = nlp(text)
    keywords = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "VERB"]]
    sentiment = TextBlob(text).sentiment.polarity
    return ', '.join(set(keywords)), round(sentiment, 2)
