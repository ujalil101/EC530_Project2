import sys
import os
import unittest
from unittest.mock import MagicMock, patch
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Modules.nlp_analysis import analyze_uploaded_pdf

class TestNLPAnalysis(unittest.TestCase):
    @patch('Modules.nlp_analysis.analyze_uploaded_pdf')
    def test_analyze_uploaded_pdf(self, mock_analyze_uploaded_pdf):
        
        # sample data
        expected_summary = "Unfortunately, she had not anticipated that others may be looking upon her from other angles, and now they were stealthily descending toward her hiding spot. She couldn't imagine that anyone would ever be able to see her in these surroundings. So there she sat, confident that she was hidden from the world and safe from danger."
        expected_sentiment = "positive"
        expected_keywords = ['stealthily descending toward', 'anyone would ever', 'others may']  

        # function to return sample data
        mock_analyze_uploaded_pdf.return_value = (expected_summary, expected_sentiment, expected_keywords)

        # call function
        sample_path = "/Users/ussie/Desktop/EC530/Project2/EC530_Project2/tests/test.pdf"
        summary, sentiment, keywords = analyze_uploaded_pdf(sample_path)

        # assert the output matches the sample data
        self.assertEqual(summary, expected_summary)
        self.assertEqual(sentiment, expected_sentiment)
        self.assertCountEqual(keywords, expected_keywords)

if __name__ == '__main__':
    unittest.main()
