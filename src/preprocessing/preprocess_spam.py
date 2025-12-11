import pandas as pd
from clean_email import clean_email

RAW_PATH = "data/raw/spam.csv"
SAVE_PATH = "data/processed/cleaned_spam.csv"

def process_spam():
    df = pd.read_csv(RAW_PATH)

    df["clean_text"] = df["text"].apply(clean_email)

    df.to_csv(SAVE_PATH, index=False)
    print("Spam dataset cleaned →", SAVE_PATH)

if __name__ == "__main__":
    process_spam()
