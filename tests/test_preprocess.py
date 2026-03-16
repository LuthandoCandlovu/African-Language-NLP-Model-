import unittest
from src.preprocess import clean_text

class TestPreprocess(unittest.TestCase):
    def test_clean_text(self):
        text = "Check this out! https://t.co/xyz @user ??"
        cleaned = clean_text(text)
        self.assertNotIn("http", cleaned)
        self.assertNotIn("@", cleaned)
        self.assertIn("smiling_face", cleaned)

if __name__ == '__main__':
    unittest.main()
