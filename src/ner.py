import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """Extracts named entities using spaCy and removes duplicates."""
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'ORG', 'GPE']:
            if ent.label_ not in entities:
                entities[ent.label_] = set()
            entities[ent.label_].add(ent.text)
    for key, value in entities.items():
        entities[key] = list(value)
    return entities