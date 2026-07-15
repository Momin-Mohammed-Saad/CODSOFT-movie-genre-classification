import re
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def to_lowercase(text):
    return text.lower()


def remove_html(text):
    return re.sub(r"<.*?>", "", text)


def remove_urls(text):
    return re.sub(r"https?://\S+|www\.\S+", "", text)


def remove_numbers(text):
    return re.sub(r"\d+", "", text)


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_extra_spaces(text):
    return re.sub(r"\s+", " ", text).strip()


def remove_stopwords(text):
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


def lemmatize_text(text):
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(words)


def preprocess_text(text):

    text = to_lowercase(text)
    text = remove_html(text)
    text = remove_urls(text)
    text = remove_numbers(text)
    text = remove_punctuation(text)
    text = remove_extra_spaces(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)

    return text