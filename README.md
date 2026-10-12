# SMS Spam Message Classifier

## 1. Project Overview

The **SMS Spam Message Classifier** is a machine learning project that classifies SMS messages into two categories: **Spam** and **Legitimate (Ham)**. It uses Natural Language Processing (NLP) and TF-IDF vectorization to convert text messages into numerical features for classification.

The project includes a Jupyter Notebook for data preprocessing, model training, and evaluation, along with a standalone Python program that allows users to enter custom SMS messages and receive predictions.

## 2. Objectives

- Load, inspect, and preprocess the SMS Spam Collection dataset.
- Analyze the distribution of spam and legitimate messages.
- Convert text messages into numerical features using TF-IDF.
- Train and compare machine learning classification models.
- Evaluate the model using standard classification metrics.
- Save the trained model and TF-IDF vectorizer.
- Build an interactive program for classifying new SMS messages.

## 3. Dataset

**Dataset:** SMS Spam Collection Dataset

The dataset contains SMS messages labeled into two categories:

- **Ham:** Legitimate messages.
- **Spam:** Unwanted or potentially fraudulent messages.

The dataset is used to train and evaluate the machine learning model.

## 4. Technologies and Libraries Used

- **Python** — programming language.
- **Pandas and NumPy** — data handling and analysis.
- **Scikit-learn** — machine learning and evaluation.
- **TF-IDF Vectorizer** — text feature extraction.
- **Multinomial Naive Bayes** — text classification.
- **Logistic Regression** — comparison classification model.
- **Matplotlib and Seaborn** — data visualization.
- **Joblib** — saving and loading trained model files.
- **Jupyter Notebook** — development and experimentation.

## 5. Project Workflow

1. Load the SMS dataset.
2. Inspect the dataset structure and class distribution.
3. Clean the text and remove invalid or duplicate records as required.
4. Separate the message text and target labels.
5. Split the data into training and testing sets.
6. Convert text into numerical features using TF-IDF.
7. Train and compare classification models.
8. Evaluate the selected model using test data.
9. Save the trained model and fitted vectorizer.
10. Test custom SMS messages using a standalone Python script.

## 6. Models Implemented

### Multinomial Naive Bayes
A probabilistic classification algorithm commonly used for text classification.

### Logistic Regression
A classification algorithm used as a comparison model.

### Final Model
**Multinomial Naive Bayes** was selected as the final model in the current implementation based on the spam F1-score.

## 7. Model Evaluation

The final model should be evaluated on held-out test data using the following metrics.

| Evaluation Metric | Result |
|---|---|
| Accuracy | Add actual score |
| Spam Precision | Add actual score |
| Spam Recall | Add actual score |
| Spam F1-Score | Add actual score |

The **confusion matrix** helps identify correctly classified messages and classification errors, including legitimate messages incorrectly predicted as spam and spam messages incorrectly predicted as legitimate.

**Important:** Replace each placeholder with the actual result from your notebook's classification report. Do not enter estimated scores.

## 8. Project Structure

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
    ├── SMSSpamCollection
    └── readme
```

This structure reflects the files used in the project. If your actual folder or filenames differ, update the structure accordingly.

## 9. Installation and Setup

### Prerequisites
- Python 3
- pip
- Jupyter Notebook (for running the notebook)

### Step 1: Install Dependencies

Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

### Step 2: Run the Jupyter Notebook

Run:

```bash
jupyter notebook Spam_Message_Classifier.ipynb
```

Execute the cells in order to inspect the dataset, train the model, and view the evaluation results.

### Step 3: Run the Standalone Spam Checker

Ensure that the `models` folder contains both saved model files. Then execute:

```bash
python "python spam_checker.py"
```

Enter an SMS message when prompted. The program displays either `SPAM MESSAGE` or `LEGITIMATE MESSAGE`.

Type `exit` to stop the program.

## 10. Sample Prediction Logs

The following examples show the observed outputs from testing the current standalone program.

### Test 1: Prize Message

**Input:**
```text
Congratulations! You have won a free prize. Claim your reward now!
```

**Output:**
```text
Result: SPAM MESSAGE
```

### Test 2: Personal Message

**Input:**
```text
Hi, I have reached college. Meet me near the library after class.
```

**Output:**
```text
Result: LEGITIMATE MESSAGE
```

### Test 3: Suspicious Bank Message

**Input:**
```text
URGENT: Your bank account will be suspended! Verify your details immediately by clicking this link.
```

**Output:**
```text
Result: LEGITIMATE MESSAGE
```

The third example demonstrates that the current model can misclassify suspicious messages. The predictions shown above are examples from the current testing session; results can vary if the model or vectorizer is changed.

## 11. Saved Model Files

- **`models/spam_model.pkl`** — saved Multinomial Naive Bayes classification model.
- **`models/tfidf_vectorizer.pkl`** — fitted TF-IDF vectorizer used to transform message text into numerical features.

Both files are required by the standalone spam checker.

## 12. Limitations

- The classifier may incorrectly classify some messages.
- New spam patterns may not match patterns learned from the training dataset.
- A message that appears suspicious to a person may still be classified as legitimate.
- Model performance depends on dataset quality, preprocessing, and the selected classification algorithm.

The predictions should be treated as automated classifications rather than a guarantee that a message is safe.

## 13. Conclusion

The SMS Spam Message Classifier demonstrates how Natural Language Processing and machine learning can be used to classify text messages. The project covers data preprocessing, TF-IDF feature extraction, model training, evaluation, model persistence, and interactive prediction.

The saved model and standalone Python program allow users to test new messages without retraining the classifier each time.

## 14. Author

**Kuntamukkala Lakeshini Sree**

**Project:** SMS Spam Message Classifier  
**Program:** CodeNova AI/ML Internship — Task 2
