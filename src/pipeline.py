from src.data_ingestion import read_file
from src.preprocessing import preprocess_text
from src.ner import extract_entities
from src.sentiment import analyze_sentiment
from src.wordcloud_gen import generate_wordcloud
from src.tfidf_keywords import calculate_tfidf

def run_pipeline(file_path):
    """Main pipeline function."""
    text = read_file(file_path)
    if text is None:
        return None

    tokens = preprocess_text(text)
    entities = extract_entities(text)
    sentiment = analyze_sentiment(text)
    top_keywords = calculate_tfidf(tokens, [text])
    generate_wordcloud(tokens)

    results = {
        "entities": entities,
        "sentiment": sentiment,
        "keywords": top_keywords,
    }
    return results