from flask import Flask, request, jsonify
from flask_cors import CORS
from src.predict import SentimentPredictor
from src.utils import load_config

app = Flask(__name__)
CORS(app)

predictor = SentimentPredictor()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    text = data['text']
    result = predictor.predict(text)
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    config = load_config()
    app.run(host=config['api']['host'], port=config['api']['port'])
