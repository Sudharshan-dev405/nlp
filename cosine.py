from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Sample documents ---
docs = [
    "Natural language processing is fun",
    "Machine learning is a part of artificial intelligence",
    "Natural language processing deals with text data"
]

# --- TF-IDF ---
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

# --- Cosine Similarity ---
cos_sim = cosine_similarity(tfidf_matrix)

print("Cosine Similarity Matrix:\n")
print(cos_sim)