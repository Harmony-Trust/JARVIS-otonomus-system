# 🚀 AI Content Analyzer - spaCy Example

import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_content(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return {"entities": entities}