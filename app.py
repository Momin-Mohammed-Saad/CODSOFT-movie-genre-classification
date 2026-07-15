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

# user input
movie_description =  st.text_area(
    "Enter Movie Description",
    height = 250,
    placeholder="Example: A young boy discovers he has magical powers and attends a school of wizardry..."
)

# prediction Button
predict_button = st.button("Predict Genre")

if predict_button:
    st.write("Input Received ✅")
    st.write(movie_description)

    