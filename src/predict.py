import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from src.preprocess import clean_text
from src.utils import load_config

class SentimentPredictor:
    def __init__(self, model_path=None):
        config = load_config()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        if model_path is None:
            model_path = config['model']['save_path']
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path).to(self.device)
        self.model.eval()
        self.id2label = {0: "negative", 1: "neutral", 2: "positive"}

    def predict(self, text):
        clean = clean_text(text)
        inputs = self.tokenizer(clean, return_tensors='pt', truncation=True, padding=True, max_length=128).to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.softmax(outputs.logits, dim=-1)
            pred = torch.argmax(probs, dim=-1).item()
        return {
            'text': text,
            'sentiment': self.id2label[pred],
            'confidence': probs[0][pred].item(),
            'probabilities': {self.id2label[i]: probs[0][i].item() for i in range(3)}
        }
