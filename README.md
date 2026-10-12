
readme_content = """# Spam Message Classifier

## Project Overview
This project classifies SMS messages as Spam or Legitimate (Ham)
using Natural Language Processing (NLP) and Machine Learning.

## Dataset
SMS Spam Collection Dataset containing labeled SMS messages.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Matplotlib and Seaborn
- Joblib

## Models Implemented
1. Multinomial Naive Bayes
2. Logistic Regression

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## Best Model
Multinomial Naive Bayes, selected based on the Spam F1-score.

## Saved Files
- models/spam_model.pkl
- models/tfidf_vectorizer.pkl

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Open Spam_Message_Classifier.ipynb in Jupyter Notebook.
3. Run the notebook cells from top to bottom.
4. Enter a custom SMS message to test the prediction.

## Sample Results
The model predicts whether a message is Spam or Legitimate.

Note: Results depend on the dataset and the test message.
"""

with open(r"C:\Users\lakes\OneDrive\Desktop\CodeNova\Task-2\README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md created successfully!")
