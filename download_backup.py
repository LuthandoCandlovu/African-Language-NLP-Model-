from huggingface_hub import hf_hub_download
import pandas as pd
import os

print("🔄 Downloading AfriSenti via Hugging Face hub...")

# Language code for isiZulu
lang = "zul"

# Download each split
files = {}
for split in ["train", "dev", "test"]:
    try:
        path = hf_hub_download(
            repo_id="shmuhammad/AfriSenti-twitter-sentiment",
            filename=f"data/{lang}/{split}.tsv",
            repo_type="dataset"
        )
        files[split] = path
        print(f"Downloaded {split} to {path}")
    except Exception as e:
        print(f"Could not download {split}: {e}")

# Load and combine
all_data = []
for split, path in files.items():
    df = pd.read_csv(path, sep='\t')
    print(f"{split}: {len(df)} samples")
    all_data.append(df)

if all_data:
    combined = pd.concat(all_data, ignore_index=True)
    combined = combined.rename(columns={"tweet": "text"})
    label_map = {"positive": 2, "neutral": 1, "negative": 0}
    combined["label"] = combined["label"].map(label_map)
    
    output = "data/raw/afrisenti_zulu_complete.csv"
    combined.to_csv(output, index=False)
    print(f"\n✅ Saved {len(combined)} samples")
    print(combined['label'].value_counts())
