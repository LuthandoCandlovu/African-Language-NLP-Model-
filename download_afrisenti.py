from datasets import load_dataset
import pandas as pd

print("🔄 Downloading AfriSenti for isiZulu...")
# Load the dataset (public, no login needed)
ds = load_dataset("shmuhammad/AfriSenti-twitter-sentiment", "zul", trust_remote_code=True)

# Convert to DataFrame
df = pd.DataFrame({
    'text': ds['train']['text'],
    'label': ds['train']['label']
})

# Save to raw data folder
df.to_csv("data/raw/afrisenti_zulu.csv", index=False)
print(f"✅ Saved {len(df)} samples to data/raw/afrisenti_zulu.csv")
print(df['label'].value_counts())
