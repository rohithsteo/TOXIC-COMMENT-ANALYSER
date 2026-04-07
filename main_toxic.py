import pickle

# Load model
with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

def predict(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    prob = model.predict_proba(X)[0]

    if prediction == 1:
        print("\nToxic Comment Detected")
        print("Confidence:", round(max(prob), 2))
    else:
        print("\nNormal Comment")
        print("Confidence:", round(max(prob), 2))

def main():
    print("=== Toxic Comment Detector ===")

    while True:
        text = input("\nEnter comment (or type 'exit'): ")

        if text.lower() == "exit":
            break

        predict(text)

if __name__ == "__main__":
    main()
