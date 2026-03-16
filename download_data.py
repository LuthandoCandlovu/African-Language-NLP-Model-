import os
from datasets import load_dataset
import pandas as pd

print("🔄 Loading Inkuba-instruct dataset for isiZulu...")
print("NOTE: You must be logged into Hugging Face (huggingface-cli login) and accept terms at https://huggingface.co/datasets/lelapa/Inkuba-instruct")

try:
    # Load the training split
    dataset = load_dataset("lelapa/lelapa_instruct_datasets_no_test_set", "zulu_train", split="train")
    
    # Extract sentiment examples
    data = []
    for item in dataset:
        if item.get('task') == 'sentiment':
            data.append({
                'text': item.get('input', ''),
                'label': item.get('output', '')
            })
    
    df = pd.DataFrame(data)
    sentiment_map = {'negative': 0, 'neutral': 1, 'positive': 2}
    df['label'] = df['label'].map(sentiment_map)
    
    output = "data/raw/inkuba_sentiment_zulu.csv"
    df.to_csv(output, index=False)
    print(f"✅ Saved {len(df)} samples to {output}")
    print(df['label'].value_counts())
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTrying alternative: AfriSenti direct download...")
    try:
        ds = load_dataset("shmuhammad/AfriSenti-twitter-sentiment", "zul", split="train")
        df = pd.DataFrame({'text': ds['text'], 'label': ds['label']})
        df.to_csv("data/raw/afrisenti_zulu.csv", index=False)
        print("✅ AfriSenti dataset downloaded.")
    except Exception as e2:
        print(f"❌ Also failed: {e2}")
