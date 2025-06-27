# 🔖 Fake News Detector using Machine Learning

This is a web app that predicts whether a news article is **REAL** or **FAKE** using a machine learning model trained on real-world news data. It is built with **Python**, **Scikit-learn**, and **Gradio**, and deployed on **Hugging Face Spaces**.

---

## 🔍 Features

* Cleaned and preprocessed fake/real news data
* Vectorization using **TF-IDF**
* Classification using **Logistic Regression**
* Web interface using **Gradio**
* Hosted publicly on Hugging Face

---

## 🚀 How It Works

1. You enter a news headline or article.
2. The app:

   * Cleans the text
   * Removes stopwords
   * Converts it into numerical vectors using TF-IDF
   * Passes it to a trained logistic regression model
3. It predicts: **REAL** ✅ or **FAKE** ❌

---

## 🧐 Tech Stack

| Component       | Technology          |
| --------------- | ------------------- |
| Language        | Python              |
| ML Library      | Scikit-learn        |
| Text Processing | NLTK, Regex         |
| Model           | Logistic Regression |
| Frontend        | Gradio              |
| Deployment      | Hugging Face Spaces |

---

## 📂 Project Files

| File                  | Purpose                            |
| --------------------- | ---------------------------------- |
| `app.py`              | Main Gradio web app code           |
| `fake_news_model.pkl` | Trained machine learning model     |
| `vectorizer.pkl`      | TF-IDF text vectorizer             |
| `requirements.txt`    | Python package dependencies        |
| `notebook.ipynb`      | (Optional) model training notebook |

---

## 🌐 Live Demo  ### 🌐 Live Demo
[📰 Click here to try the Fake News Detector](https://bhupesh0111-fake-news-bhupesh.hf.space)


Hosted on Hugging Face Spaces:

> ⬇️ Replace with your actual URL:
> **[https://your-username-fake-news-app.hf.space](https://your-username-fake-news-app.hf.space)**

---

## 🙋‍♂️ About the Author

Built by **Bhupesh**
📧 [bhupeshk754@gmail.com](mailto:bhupeshk754@gmail.com)
Learning machine learning & deep learning one project at a time.

---

## ✨ Future Improvements

* Add deep learning (e.g., LSTM or BERT)
* Enable real-time news scraping
* Improve text cleaning with lemmatization
* UI design enhancements
