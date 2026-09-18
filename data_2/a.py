import pandas as pd
import glob
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load notices
files = glob.glob("data_2/notices/*.csv")
notices = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Load labelled pairs
pairs = pd.read_csv("data_2/labelled_pairs.csv")

# Create notice lookup
notice_text = (
    notices["title"].fillna("") + " " +
    notices["body"].fillna("")
).str.lower()

notice_lookup = dict(zip(notices["notice_id"], notice_text))

# Get text for each pair
pairs["text_a"] = pairs["notice_id_a"].map(notice_lookup)
pairs["text_b"] = pairs["notice_id_b"].map(notice_lookup)

# Combine texts so the same TF-IDF vocabulary is used
all_text = pd.concat([pairs["text_a"], pairs["text_b"]])

# WORD representation: 1-2 grams
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    min_df=2
)

X = vectorizer.fit_transform(all_text)

A = X[:len(pairs)]
B = X[len(pairs):]

pairs["word_similarity"] = [
    cosine_similarity(A[i], B[i])[0, 0]
    for i in range(len(pairs))
]

print("\nRESULTS")
print(pairs.groupby("label")["word_similarity"].describe())

print("\nMean similarity:")
print(pairs.groupby("label")["word_similarity"].mean())
