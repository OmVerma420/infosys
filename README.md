# 📧 Email Classification & Urgency Detection System  
### *(Milestone 1 – Data Collection & Preprocessing)*

---

## 📌 Project Overview

This project focuses on building an **AI-powered Email Classification & Urgency Detection System**.  
It categorizes emails into multiple classes and assigns urgency levels (low, medium, high).  

This submission contains **Milestone 1**, which involves dataset preparation and preprocessing.

---

## 🎯 Milestone 1 – Objective

> **Prepare a clean, labeled dataset for training NLP models.**

### ✔ Tasks Completed

- Collected email datasets  
- Cleaned HTML, signatures, URLs  
- Normalized email subjects & bodies  
- Removed noise (punctuation, stopwords, casing)  
- Applied lemmatization  
- Created structured CSVs  
- Assigned urgency levels  
- Saved processed datasets  

---

## 📂 Project Structure

```text
infosys/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   ├── priority.csv
│   │   ├── emailclass.csv
│   │   ├── spam.csv
│   │
│   └── processed/
│       ├── cleaned_priority.csv
│       ├── cleaned_emailclass.csv
│       ├── cleaned_spam.csv
│
├── src/
│   ├── preprocessing/
│   │   ├── clean_text.py
│   │   ├── preprocess_priority.py
│   │   ├── preprocess_emailclass.py
│   │   └── preprocess_spam.py
│
└── venv/   # ignored by .gitignore


yaml
Copy code

---

## 🧹 Preprocessing Steps Applied

1. Lowercase conversion  
2. Remove email addresses  
3. Remove URLs  
4. Strip HTML tags  
5. Remove punctuation  
6. Remove stopwords  
7. Apply lemmatization  
8. Combine subject + body (when available)  
9. Add urgency labels  
10. Save cleaned structured CSV files  

---

## 🧪 Running the Preprocessing Scripts

### 1️⃣ Activate virtual environment

```sh
.\venv\Scripts\activate
2️⃣ Install dependencies
sh
Copy code
pip install -r requirements.txt
3️⃣ Download NLTK resources
sh
Copy code
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('omw-1.4')"
4️⃣ Run preprocessing scripts
sh
Copy code
python src/preprocessing/preprocess_priority.py
python src/preprocessing/preprocess_emailclass.py
python src/preprocessing/preprocess_spam.py
✔ Output saved at:
bash
Copy code
data/processed/cleaned_priority.csv  
data/processed/cleaned_emailclass.csv  
data/processed/cleaned_spam.csv
📊 Example Cleaned Output
subject	body	cleaned_text	category	urgency
Internet Issue	My internet is not working	internet work	complaint	high
Refund Request	Want refund status	refund status know	request	medium

📜 License
This project uses the MIT License as required.

🚀 Upcoming Milestones
Milestone 2 (Weeks 3–4)
Train Logistic Regression, Naive Bayes

Fine-tune BERT/DistilBERT

Evaluate accuracy

Milestone 3 (Weeks 5–6)
Urgency detection model

Combine ML + rule-based signals

Milestone 4 (Weeks 7–8)
Dashboard with filters

Deploy using Azure/AWS/GCP

👤 Author
Om Verma
Infosys Springboard – AI Email Classification Project