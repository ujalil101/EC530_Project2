import fitz
import re
from collections import Counter
from textblob import TextBlob
from rake_nltk import Rake
 
# extract text from pdf
def extract_text_from_pdf(pdf_file_path):
    text = ""
    with fitz.open(pdf_file_path) as doc:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
    return text

def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return sentences

# calculate word frequency in sentences
def calculate_word_frequency(sentence):
    # convert sentences to words
    words = re.findall(r'\w+', sentence.lower())
    # count word freq
    word_freq = Counter(words)
    return word_freq

# score sentences based on word frequency
def score_sentences(sentences):
    sentence_scores = {}
    for sentence in sentences:
        # calc word freq for current sentence
        word_freq = calculate_word_frequency(sentence)
        # sum  frequencies of all words in the sentence to score
        score = sum(word_freq.values())
        # store sentence score in sentence_scores
        sentence_scores[sentence] = score
    return sentence_scores

# generate summary 
def generate_summary(text, num_sentences=3):
    # preprocess text and split into sentences
    sentences = preprocess_text(text)
    # score sentences based on word freq
    sentence_scores = score_sentences(sentences)
    # sort sentences based on their scores 
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    # select top N setnences
    summary = ' '.join(sorted_sentences[:num_sentences])
    return summary

# find top N keywords using RAKE algorithm
def find_keywords_rake(text, top_n=7):
    
    r = Rake(max_length=3)
    # extract key words
    r.extract_keywords_from_text(text)
    # get top n ranked
    keywords = r.get_ranked_phrases()[:top_n]
    # remove dups
    unique_keywords = list(set(keywords))

    return unique_keywords


# sentiment analysis
def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    # get sentiment polarity score (-1 to 1) from textblob
    sentiment_score = blob.sentiment.polarity
    # get sentiment label based on the polarity score
    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return sentiment

# analyze analyze uploaded PDF
def analyze_uploaded_pdf(pdf_file_path):
    # get text from PDF
    text = extract_text_from_pdf(pdf_file_path)
    # generate summary
    summary = generate_summary(text)
    # get top key wrods
    keywords = find_keywords_rake(text)
    # perform sentiment analysis
    sentiment = perform_sentiment_analysis(text)
    
    return summary, sentiment, keywords
