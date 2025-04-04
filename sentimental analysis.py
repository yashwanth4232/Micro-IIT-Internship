import pandas as pd
import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import urllib.request
nltk.download("stopwords")
nltk.download("punkt")
try:
    nltk.data.find("tokenizers/punkt_tab/english/")
except LookupError:
    nltk.download("punkt_tab")

def preprocess_text(text):
    if pd.isna(text):
        return ""
    text = text.lower() 
    text = re.sub(r"\d+", "", text) 
    text = text.translate(str.maketrans("", "", string.punctuation)) 
    tokens = word_tokenize(text) 
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)
file_url = "https://drive.google.com/uc?id=1-jJfHxQEExSWoL83pmU9BnIyUg5D4Lw_"
try:
    file_path, _ = urllib.request.urlretrieve(file_url, "dataset.csv")
    df = pd.read_csv(file_path, encoding="utf-8")
    print("Dataset loaded successfully")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()
expected_columns = ["text", "sentiment"]
if not all(col in df.columns for col in expected_columns):
    print("Dataset must contain 'text' and 'sentiment' columns")
    print("Available Columns:", df.columns)
    exit()
df["processed_text"] = df["text"].apply(preprocess_text)
X_train, X_test, y_train, y_test = train_test_split(
    df["processed_text"], df["sentiment"], test_size=0.2, random_state=42
)
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
print("Model trained successfully")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

def predict_sentiment(text):
    processed_text = preprocess_text(text)
    prediction = model.predict([processed_text])[0]
    return prediction
while True:
    user_input = input("Enter a statement to analyze sentiment (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    sentiment = predict_sentiment(user_input)
    print(f"Sentiment: {sentiment}")
