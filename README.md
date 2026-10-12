# SMS Spam Message Classifier

## Project Overview
The **SMS Spam Message Classifier** is a machine learning project that classifies SMS messages into two categories: **Spam** and **Legitimate (Ham)**. It uses Natural Language Processing (NLP) techniques to convert text messages into numerical features and predict whether a message is spam or legitimate.

The project includes a Jupyter Notebook for data analysis, model training, and evaluation, along with a standalone Python program for checking messages.

## Objectives
- Analyze and preprocess the SMS Spam Collection dataset.
- Convert text messages into numerical features using TF-IDF.
- Train and evaluate machine learning classification models.
- Identify spam and legitimate messages.
- Save the trained model and vectorizer for reuse.
- Test new messages using a standalone Python script.

## Dataset
**SMS Spam Collection Dataset**

The dataset contains SMS messages labeled as:
- **Ham:** Legitimate messages.
- **Spam:** Unwanted or potentially fraudulent messages.

The dataset is used to train and evaluate the classifier.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- TF-IDF Vectorization
- Multinomial Naive Bayes
- Logistic Regression
- Matplotlib and Seaborn
- Joblib
- Jupyter Notebook

## Project Workflow
1. Load the SMS dataset.
2. Inspect and clean the data.
3. Analyze the distribution of spam and legitimate messages.
4. Split the dataset into training and testing sets.
5. Convert text messages into numerical features using TF-IDF.
6. Train machine learning classification models.
7. Evaluate model performance using classification metrics.
8. Save the trained model and TF-IDF vectorizer.
9. Test new SMS messages using the standalone program.

## Models Implemented
1. **Multinomial Naive Bayes**
2. **Logistic Regression**

Multinomial Naive Bayes was selected as the final model in the current implementation.

## Evaluation Metrics
The model can be evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics help assess how well the classifier distinguishes spam from legitimate messages.

## Project Structure
```text
Task-2/
├── Spam_Message_Classifier.ipynb
├── python spam_checker.py
├── README.md
├── requirements.txt
├── models/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
├── screenshots/
└── sms+spam+collection/
    └── SMSSpamCollection
```

## Installation and Setup

### 1. Install Python
Install Python 3 if it is not already installed.

### 2. Install Dependencies
Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter Notebook
Open the notebook:

```bash
jupyter notebook Spam_Message_Classifier.ipynb
```

Run the cells to inspect the dataset, train the model, and review the evaluation results.

### 4. Run the Standalone Spam Checker
Ensure the `models` folder contains both saved model files. Then run:

```bash
python "python spam_checker.py"
```

Enter an SMS message when prompted. The program will display either `SPAM MESSAGE` or `LEGITIMATE MESSAGE`.

Type `exit` to close the program.

## Sample Testing
Example spam message:

```text
Congratulations! You have won a free prize. Claim your reward now!
```

Example legitimate message:

```text
Hi, I have reached college. Meet me near the library after class.
```

The program displays its prediction for each entered message. Actual predictions may vary depending on the trained model.

## Saved Model Files
- `models/spam_model.pkl` — trained classification model.
- `models/tfidf_vectorizer.pkl` — fitted TF-IDF vectorizer used to transform messages.

## Limitations
- The classifier may misclassify some messages.
- Suspicious messages are not always detected as spam.
- The model's performance depends on the dataset and the patterns learned during training.

## Conclusion
This project demonstrates how Natural Language Processing and machine learning can be used to classify SMS messages. It provides a reusable trained model and a standalone interface for testing new messages.

## Author
**Kuntamukkala Lakeshini Sree**

CodeNova AI/ML Internship — Task 2
