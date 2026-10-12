
import joblib

# Load the saved model and vectorizer
model = joblib.load("models/spam_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

print("=== SMS Spam Message Checker ===")

while True:
    message = input("\nEnter a message (or type 'exit' to quit): ")

    if message.lower() == "exit":
        print("Thank you for using Spam Checker!")
        break

    message_tfidf = vectorizer.transform([message])
    prediction = model.predict(message_tfidf)[0]

    if prediction == 1:
        print("Result: SPAM MESSAGE")
    else:
        print("Result: LEGITIMATE MESSAGE")
