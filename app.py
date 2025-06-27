import gradio as gr
import joblib
import re
from nltk.corpus import stopwords
import nltk
import os

nltk.download('stopwords')

# Load saved model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
stop_words = set(stopwords.words("english"))

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return " ".join(word for word in text.split() if word not in stop_words)

# Prediction function
def predict_news(news):
    cleaned = clean_text(news)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return "REAL ✅" if prediction == 1 else "FAKE ❌"

# Gradio interface
interface = gr.Interface(
    fn=predict_news,
    inputs="text",
    outputs="text",
    title="📰 Fake News Detector by Bhupesh",
    description="Enter a news article or headline to check if it's REAL or FAKE. Created by Bhupesh • Contact: bhupesh@gmail.com",
)

interface.launch()
