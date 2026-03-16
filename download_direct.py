import pandas as pd
import requests
import os

print("🔄 Downloading AfriSenti for isiZulu directly from GitHub...")

# Direct URLs to the TSV files (from the dataset source code)
base_url = "https://raw.githubusercontent.com/afrisenti-semeval/afrisent-semeval-2023/main/data/zul"
files = {
    "train": f"{base_url}/train.tsv",
    "dev": f"{base_url}/dev.tsv",
    "test": f"{base_url}/test.tsv"
}

all_data = []

for split, url in files.items():
    print(f"Downloading {split} split...")
    try:
        df = pd.read_csv(url, sep='\t')
        print(f"  Found {len(df)} samples")
        all_data.append(df)
    except Exception as e:
        print(f"  Error: {e}")

if all_data:
    # Combine all splits
    combined = pd.concat(all_data, ignore_index=True)
    
    # Rename columns to match our expected format
    combined = combined.rename(columns={"tweet": "text"})
    
    # Map labels to numbers
    label_map = {"positive": 2, "neutral": 1, "negative": 0}
    combined["label"] = combined["label"].map(label_map)
    
    # Save to raw data folder
    output_path = "data/raw/afrisenti_zulu_complete.csv"
    combined.to_csv(output_path, index=False)
    print(f"\n✅ Saved {len(combined)} total samples to {output_path}")
    print(f"Label distribution:\n{combined['label'].value_counts()}")
else:
    print("❌ No data downloaded. Check your internet connection.")
