import pandas as pd
from clean_email import clean_email
import os

def process_emailclass():

    input_path = "data/raw/emailclass.csv"
    output_path = "data/processed/cleaned_emailclass.csv"

    if not os.path.exists(input_path):
        print(f"ERROR: File not found → {input_path}")
        return

    df = pd.read_csv(input_path)

    # Fix column names
    df.columns = df.columns.str.strip().str.lower()

    print("Columns found:", df.columns)

    # Validate column names
    if "text" not in df.columns or "type" not in df.columns:
        print("ERROR: Columns ['text', 'type'] not found!")
        return

    # Clean the text
    df["clean_text"] = df["text"].astype(str).apply(clean_email)

    # Rename type → label (ML friendly)
    df.rename(columns={"type": "label"}, inplace=True)

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print(f"EmailClass dataset cleaned → {output_path}")


if __name__ == "__main__":
    process_emailclass()
