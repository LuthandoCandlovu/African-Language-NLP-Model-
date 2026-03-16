import unittest
from src.predict import SentimentPredictor

class TestModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.predictor = SentimentPredictor()

    def test_prediction(self):
        text = "Ngiyakuthanda lo mkhiqizo!"  # "I love this product!" in isiZulu
        result = self.predictor.predict(text)
        self.assertIn('sentiment', result)
        self.assertIn('confidence', result)

if __name__ == '__main__':
    unittest.main()
