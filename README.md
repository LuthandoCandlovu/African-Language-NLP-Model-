# African Language NLP – Sentiment Analysis for isiXhosa/isiZulu

This project builds a state-of-the-art sentiment analysis model for South African languages (isiXhosa and isiZulu) using transformer models. It includes:

- Data collection scripts (Twitter, NCHLT corpus)
- Preprocessing pipeline tailored for Nguni languages
- Fine-tuning of multilingual transformers (XLM-R, AfriBERTa)
- REST API for real-time inference
- Unit tests and configuration management

## ?? Quick Start

1. Clone the repo.
2. Install dependencies: pip install -r requirements.txt
3. Prepare your data (place CSV files in data/raw/ with columns 	ext and label).
4. Run preprocessing: python -c "from src.preprocess import prepare_datasets; from src.utils import load_config; prepare_datasets(load_config())"
5. Train the model: python src/train.py
6. Start the API: python api/app.py
7. Send a POST request to http://localhost:5000/predict with JSON {"text": "your sentence"}.

## ?? Model Performance

(Add your results here after training)

## ?? Why This Matters

African languages are underrepresented in NLP. This project aims to bridge that gap and provide tools for businesses, researchers, and communities.

## ?? Contributing

Pull requests welcome! Help us add more data, improve preprocessing, or extend to other languages.

## ?? License

MIT
