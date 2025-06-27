import gradio as gr
import joblib
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


# Load model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Clean text function
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()
    text = " ".join(word for word in text.split() if word not in stop_words)
    return text

# Prediction function
def predict_news(news):
    cleaned = clean_text(news)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)
    return "REAL ✅" if prediction[0] == 1 else "FAKE ❌"

# Gradio interface
gr.Interface(fn=predict_news, inputs="text", outputs="text", title="Fake News Detector").launch()
