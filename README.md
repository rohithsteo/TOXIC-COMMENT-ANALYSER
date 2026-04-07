# 🚨 Toxic Comment Detector (NLP)

A machine learning-based system that detects whether a comment is toxic or normal using Natural Language Processing.

---

## 🧠 Overview

This project uses TF-IDF vectorization and Logistic Regression to classify text as toxic or non-toxic.

It simulates real-world content moderation systems used in social media platforms.

---

## ⚙️ Features

- Text classification (toxic / normal)
- Confidence score output
- Lightweight ML model
- Interactive CLI interface

---

## 🛠️ Tech Stack

- Python
- Scikit-learn (TF-IDF + Logistic Regression)

---

## 📂 Project Structure

train_model.py   # Train model  
main.py          # Run detector  
model.pkl        # Saved model  
requirements.txt  
README.md  

---

## 🚀 How to Run

1. Install dependencies  
pip install -r requirements.txt  

2. Train the model  
python train_model.py  

3. Run the detector  
python main.py  

---

## 🧠 How It Works

- Converts text into numerical vectors (TF-IDF)
- Trains a Logistic Regression classifier
- Predicts whether input text is toxic

---

## 🎯 Example

Input:  
"I hate you"  

Output:  
Toxic Comment Detected  
Confidence: 0.91  

---

## 📌 Future Improvements

- Use real datasets (Kaggle)
- Deep learning (LSTM / Transformers)
- Web app interface
- API deployment

---

## 👨‍💻 Author

Rohith Raj  

---

## ⭐ Star this repo if you like it!
