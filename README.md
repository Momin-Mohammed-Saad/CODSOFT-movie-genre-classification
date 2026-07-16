    # 🎬 Movie Genre Classification using NLP

A Machine Learning project that predicts the genre of a movie based on its plot summary using Natural Language Processing (NLP) techniques.

---

## 📌 Project Overview

Movie plot summaries contain rich textual information that can be used to identify the genre of a movie. In this project, Natural Language Processing (NLP) techniques were applied to preprocess movie descriptions, convert them into numerical features using TF-IDF, and train multiple machine learning models for genre classification.

The project compares the performance of different classifiers and selects the best-performing model for prediction.

---

## 📂 Dataset

**Dataset Name:** Genre Classification Dataset - IMDb

Dataset contains:

- Train Dataset
- Test Dataset
- Test Labels
- Dataset Description

**Total Training Samples:** 54,214

**Input Feature:**

- Movie Description

**Target Feature:**

- Genre

---

## ⚙️ Project Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Text Preprocessing
4. TF-IDF Feature Extraction
5. Model Training
6. Model Evaluation
7. Model Comparison
8. Best Model Selection

---

## 📁 Project Structure

```
movie-genre-classification/
│
├── data/
├── models/
│   ├── best_model.joblib
│   └── tfidf_vectorizer.joblib
├── notebooks/
│   ├── 01_Data_Loading_EDA.ipynb
│   ├── 02_Text_Preprocessing_TFIDF.ipynb
│   └── 03_Model_Training_Evaluation.ipynb
├── app.py
├── text_preprocessing.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Machine (Linear SVM)

---

## 📊 Model Performance

| Model | Accuracy | Macro F1 Score |
|--------|----------|----------------|
| Multinomial Naive Bayes | 52.03% | 0.1670 |
| Logistic Regression | **58.56%** | 0.3016 |
| Linear SVM | 57.35% | **0.3382** |

**Best Model (Accuracy):** Logistic Regression

---

## 📈 Results

- Successfully classified movie genres using NLP techniques.
- Converted textual movie descriptions into TF-IDF feature vectors.
- Compared three different machine learning algorithms.
- Logistic Regression achieved the highest overall accuracy.
- Saved the trained model and TF-IDF vectorizer for future deployment.

---

## ✨ Features

- Predicts movie genres from plot summaries
- NLP-based text preprocessing
- TF-IDF feature extraction
- Logistic Regression classifier
- Interactive Streamlit web application
- Trained model saved using Joblib

---

## 🚀 Installation

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

## 👨‍💻 Author

**Momin Saad**
