import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from Modules.nlp_analysis import analyze_uploaded_pdf

def test_analyze_uploaded_pdf():
    # sample pdf 
    sample_path = "/Users/ussie/Desktop/EC530/Project2/EC530_Project2/uploads/test.pdf"
    # analyze pdf function
    summary, sentiment, keywords = analyze_uploaded_pdf(sample_path)

    # expected summary
    expected_summary = "Unfortunately, she had not anticipated that others may be looking upon her from other angles, and now they were stealthily descending toward her hiding spot. She couldn't imagine that anyone would ever be able to see her in these surroundings. So there she sat, confident that she was hidden from the world and safe from danger."
    # expected sentiment
    expected_sentiment = "positive"
    # expected keywords
    expected_keywords = ['stealthily descending toward', 'anyone would ever', 'others may', 'spot', 'looking upon', 'hiding spot']

    # test
    assert summary == expected_summary
    assert sentiment == expected_sentiment
    assert set(keywords) == set(expected_keywords)

