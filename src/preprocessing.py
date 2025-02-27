import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def preprocess_text(text):
    """Performs tokenization, stopword removal, and lemmatization."""
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    stop_words.update(['ai', 'however', 'despite', 'even', 'also'])
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return lemmatized_tokens

