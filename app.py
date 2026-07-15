import streamlit as st
import joblib

# Page Configuration
st.set_page_config(
    page_title="Movie Genre Classification",
    page_icon="🎬",
    layout="centered"
)

# Load trained model and TF-IDF vectorizer
model = joblib.load("models/best_model.joblib")
vectorizer = joblib.load("models/tfidf_vectorizer.joblib")

# App Title
st.title("🎬 Movie Genre Classification")

st.write("Predict the genre of a movie using its plot summary.")