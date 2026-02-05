# CODETECH TASK 1 – TEXT SUMMARIZATION TOOL
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
import re
import heapq
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords


def preprocess(text):
    text = re.sub(r'\s+', ' ', text)
    return text


def sentence_tokenize(text):
    return nltk.sent_tokenize(text)


def word_frequencies(text):
    words = nltk.word_tokenize(text.lower())

    stop_words = stopwords.words('english')

    words = [word for word in words if word.isalnum() and word not in stop_words]

    freq = Counter(words)

    max_freq = max(freq.values())

    for word in freq.keys():
        freq[word] = freq[word] / max_freq

    return freq


def summarize(text, n=2):

    text = preprocess(text)

    sentences = sentence_tokenize(text)

    freq = word_frequencies(text)

    scores = {}

    for sent in sentences:
        for word in nltk.word_tokenize(sent.lower()):
            if word in freq.keys():
                scores[sent] = scores.get(sent, 0) + freq[word]

    summary = heapq.nlargest(n, scores, key=scores.get)

    return " ".join(summary)



# ===== SAMPLE RUN =====

if __name__ == "__main__":

    sample_text = """
    Artificial Intelligence is growing rapidly in the modern world.
    It helps in education, healthcare and business automation.
    Text summarization is an important NLP application.
    It reduces long articles into short meaningful content.
    Many companies use AI based summarization tools.
    """

    print("ORIGINAL TEXT:\n")
    print(sample_text)

    print("\nSUMMARY:\n")
    print(summarize(sample_text, 2))
