import os
import pandas as pd
import glob
from src.utils import load_config

def load_raw_data(config):
    raw_path = config['data']['raw_path']
    all_files = glob.glob(os.path.join(raw_path, "*.csv"))
    df_list = []
    for f in all_files:
        df = pd.read_csv(f)
        if 'text' in df.columns and 'label' in df.columns:
            df_list.append(df[['text', 'label']])
        else:
            print(f"Warning: {f} missing required columns")
    if not df_list:
        raise ValueError("No valid data files found. Place your CSV files in data/raw/")
    combined = pd.concat(df_list, ignore_index=True)
    return combined

def load_external_nchlt(language='zulu'):
    path = f"data/external/nchlt_{language}.csv"
    if not os.path.exists(path):
        print("NCHLT data not found. Download from https://rma.nwu.ac.za/")
        return None
    df = pd.read_csv(path)
    sentiment_map = {'negative':0, 'neutral':1, 'positive':2}
    if 'sentiment' in df.columns and df['sentiment'].dtype == 'object':
        df['label'] = df['sentiment'].map(sentiment_map)
    return df[['text', 'label']]

def load_huggingface_sentiment():
    """Load AfriSenti from Hugging Face"""
    try:
        from datasets import load_dataset
        # Try loading AfriSenti (may require authentication)
        dataset = load_dataset("shmuhammad/AfriSenti-twitter-sentiment", "zul")
        return dataset
    except Exception as e:
        print(f"Access??????,??????: {e}")
        return None
