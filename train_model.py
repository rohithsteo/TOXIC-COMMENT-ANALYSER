from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Simple dataset
texts = [
    "I love this",
    "You are amazing",
    "Great work",
    "I hate you",
    "You are stupid",
    "Idiot",
    "This is terrible",
    "You are useless"
]

labels = [0, 0, 0, 1, 1, 1, 1, 1]  # 0 = normal, 1 = toxic

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model trained and saved")
