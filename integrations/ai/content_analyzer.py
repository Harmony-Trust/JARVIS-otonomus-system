# 🧠 JARVIS Module: Content Analyzer v2050 - NLP Entity & Topic Extraction

import spacy
from collections import Counter

# Load model spaCy (default: English)
try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    raise RuntimeError("❌ Model spaCy 'en_core_web_sm' tidak ditemukan. Jalankan: python -m spacy download en_core_web_sm")

def analyze_content(text: str):
    doc = nlp(text)

    # Ekstraksi entitas
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Ekstraksi kata kunci (token penting)
    keywords = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
    keyword_freq = Counter(keywords).most_common(5)

    # Ekstraksi topik (berdasarkan noun chunks)
    topics = [chunk.text for chunk in doc.noun_chunks]

    return {
        "entities": entities,
        "keywords": keyword_freq,
        "topics": topics
    }
