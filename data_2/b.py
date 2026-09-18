import pandas as pd
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.random_projection import GaussianRandomProjection
from sklearn.metrics.pairwise import cosine_similarity

# Load notices
files = glob.glob("data_2/notices/*.csv")
notices = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Load labelled pairs
pairs = pd.read_csv("data_2/labelled_pairs.csv")

# Text
text = (
    notices["title"].fillna("") + " " +
    notices["body"].fillna("")
)

lookup = dict(zip(notices["notice_id"], text))

pairs["text_a"] = pairs["notice_id_a"].map(lookup)
pairs["text_b"] = pairs["notice_id_b"].map(lookup)

all_text = pd.concat([pairs["text_a"], pairs["text_b"]])

# Full TF-IDF
tfidf = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
X = tfidf.fit_transform(all_text)

print("FULL FEATURES:", X.shape[1])

# Deliberately reduce to 512 dimensions
rp = GaussianRandomProjection(n_components=512, random_state=42)
X_reduced = rp.fit_transform(X)

A = X_reduced[:len(pairs)]
B = X_reduced[len(pairs):]

pairs["reduced_similarity"] = [
    cosine_similarity(A[i:i+1], B[i:i+1])[0, 0]
    for i in range(len(pairs))
]

print("\nREDUCED RESULTS")
print(pairs.groupby("label")["reduced_similarity"].mean())

print("\nFULL vs REDUCED")
print("Same full mean:     ", pairs.loc[pairs.label=="same", "reduced_similarity"].mean())
print("Different full mean:", pairs.loc[pairs.label=="different", "reduced_similarity"].mean())