from llama_index.readers.web import BeautifulSoupWebReader
import re
import nltk

nltk.download('punkt')


def cleanText(text):
    """Remove unnecessary characters"""
    cleaned_text = re.sub(r'\n|\r', ' ', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    """Tokenize the text into sentences"""
    sentences = nltk.tokenize.sent_tokenize(cleaned_text)

    """Extract all sentences"""
    summary = ' '.join(sentences)

    return summary


def procesLink(url):
    documents = BeautifulSoupWebReader().load_data([url])

    """Apply the summarize_text function to the document text"""
    cleanedText = cleanText(documents[0].text)

    return cleanedText


# print(summary)
# url = "https://en.wikipedia.org/wiki/Jesus"
