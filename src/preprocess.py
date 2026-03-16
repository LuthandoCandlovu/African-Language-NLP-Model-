import re
import emoji
import torch
import pandas as pd
from transformers import AutoTokenizer
from sklearn.model_selection import train_test_split
from src.data_loader import load_raw_data
from src.utils import load_config

def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)
    text = emoji.demojize(text, delimiters=(" ", " "))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def prepare_datasets(config):
    # Load raw data
    df = load_raw_data(config)
    df['clean_text'] = df['text'].apply(clean_text)

    # Split
    train_texts, temp_texts, train_labels, temp_labels = train_test_split(
        df['clean_text'], df['label'], test_size=0.3, random_state=config['training']['seed']
    )
    val_texts, test_texts, val_labels, test_labels = train_test_split(
        temp_texts, temp_labels, test_size=0.5, random_state=config['training']['seed']
    )

    # Save cleaned CSVs (optional)
    train_df = pd.DataFrame({'text': train_texts, 'label': train_labels})
    val_df = pd.DataFrame({'text': val_texts, 'label': val_labels})
    test_df = pd.DataFrame({'text': test_texts, 'label': test_labels})

    train_df.to_csv(config['data']['processed_path'] + 'train.csv', index=False)
    val_df.to_csv(config['data']['processed_path'] + 'val.csv', index=False)
    test_df.to_csv(config['data']['processed_path'] + 'test.csv', index=False)

    # Tokenize and save as PURE TENSORS
    tokenizer = AutoTokenizer.from_pretrained(config['model']['name'])
    max_len = config['model']['max_length']

    def tokenize_to_tensors(texts):
        enc = tokenizer(texts.tolist(), truncation=True, padding=True, max_length=max_len, return_tensors='pt')
        return enc['input_ids'], enc['attention_mask']

    train_ids, train_mask = tokenize_to_tensors(train_texts)
    val_ids, val_mask = tokenize_to_tensors(val_texts)
    test_ids, test_mask = tokenize_to_tensors(test_texts)

    # Convert labels to tensors
    train_labels = torch.tensor(train_labels.values)
    val_labels = torch.tensor(val_labels.values)
    test_labels = torch.tensor(test_labels.values)

    # Save as dictionary of tensors (safe with weights_only=True)
    torch.save({
        'input_ids': train_ids,
        'attention_mask': train_mask,
        'labels': train_labels
    }, config['data']['processed_path'] + 'train.pt')

    torch.save({
        'input_ids': val_ids,
        'attention_mask': val_mask,
        'labels': val_labels
    }, config['data']['processed_path'] + 'val.pt')

    torch.save({
        'input_ids': test_ids,
        'attention_mask': test_mask,
        'labels': test_labels
    }, config['data']['processed_path'] + 'test.pt')

    print("? Data preparation complete. Tensors saved.")

if __name__ == "__main__":
    config = load_config()
    prepare_datasets(config)
