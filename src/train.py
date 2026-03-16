import torch
from torch.utils.data import DataLoader, TensorDataset
from transformers import AutoModelForSequenceClassification, AutoTokenizer, get_linear_schedule_with_warmup
from torch.optim import AdamW
from sklearn.metrics import accuracy_score, f1_score
from tqdm import tqdm
from src.utils import load_config, set_seed

def load_tokenized_data(config, split='train'):
    path = config['data']['processed_path'] + f'{split}.pt'
    data = torch.load(path, weights_only=True)  # safe: only tensors
    input_ids = data['input_ids']
    attention_mask = data['attention_mask']
    labels = data['labels']
    return TensorDataset(input_ids, attention_mask, labels)

def train_epoch(model, dataloader, optimizer, scheduler, device):
    model.train()
    total_loss = 0
    for batch in tqdm(dataloader, desc="Training"):
        input_ids, attention_mask, labels = [b.to(device) for b in batch]
        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        total_loss += loss.item()
        loss.backward()
        optimizer.step()
        scheduler.step()
    return total_loss / len(dataloader)

def eval_model(model, dataloader, device):
    model.eval()
    preds, true_labels = [], []
    with torch.no_grad():
        for batch in dataloader:
            input_ids, attention_mask, labels = [b.to(device) for b in batch]
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            preds.extend(torch.argmax(logits, dim=-1).cpu().numpy())
            true_labels.extend(labels.cpu().numpy())
    acc = accuracy_score(true_labels, preds)
    f1 = f1_score(true_labels, preds, average='weighted')
    return acc, f1

def train(config):
    set_seed(config['training']['seed'])
    device = torch.device(config['training']['device'] if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    # Load datasets
    train_dataset = load_tokenized_data(config, 'train')
    val_dataset = load_tokenized_data(config, 'val')

    train_loader = DataLoader(train_dataset, batch_size=config['model']['batch_size'], shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=config['model']['batch_size'])

    # Load model
    num_labels = 3
    model = AutoModelForSequenceClassification.from_pretrained(
        config['model']['name'], num_labels=num_labels
    ).to(device)

    tokenizer = AutoTokenizer.from_pretrained(config['model']['name'])

    # Ensure learning rate is float
    lr = float(config['model']['learning_rate'])
    optimizer = AdamW(model.parameters(), lr=lr)
    total_steps = len(train_loader) * config['model']['epochs']
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

    best_f1 = 0
    for epoch in range(config['model']['epochs']):
        print(f"Epoch {epoch+1}/{config['model']['epochs']}")
        train_loss = train_epoch(model, train_loader, optimizer, scheduler, device)
        val_acc, val_f1 = eval_model(model, val_loader, device)
        print(f"Train loss: {train_loss:.4f} | Val Acc: {val_acc:.4f} | Val F1: {val_f1:.4f}")

        if val_f1 > best_f1:
            best_f1 = val_f1
            model.save_pretrained(config['model']['save_path'])
            tokenizer.save_pretrained(config['model']['save_path'])
            print("? Best model saved.")

if __name__ == "__main__":
    config = load_config()
    train(config)
