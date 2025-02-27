from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_tfidf(tokens, all_texts):
    """Calculates TF-IDF scores and returns top 10 keywords."""
    vectorizer = TfidfVectorizer(min_df=1)
    tfidf_matrix = vectorizer.fit_transform([' '.join(all_texts)])
    feature_names = vectorizer.get_feature_names_out()
    dense = tfidf_matrix.todense()
    lst1 = dense.tolist()[0]
    all_words = [(word, lst1[i]) for i, word in enumerate(feature_names)]
    top_keywords = sorted(all_words, key=lambda x: x[1], reverse=True)[:10]
    return top_keywords