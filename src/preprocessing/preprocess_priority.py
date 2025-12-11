import pandas as pd
from clean_email import clean_email
import os

RAW_PATH = "data/raw/priority.csv"
SAVE_PATH = "data/processed/cleaned_priority.csv"

def process_priority():
    df = pd.read_csv(RAW_PATH)

    df["clean_subject"] = df["subject"].apply(clean_email)
    df["clean_body"] = df["body"].apply(clean_email)

    # urgency already present in dataset (LOW / MEDIUM / HIGH)
    df["urgency"] = df["priority"]

    df.to_csv(SAVE_PATH, index=False)
    print("Priority dataset cleaned and saved →", SAVE_PATH)

if __name__ == "__main__":
    process_priority()
