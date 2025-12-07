import re
import csv
import nltk
from nltk.corpus import stopwords

try:
    nltk.data.find("corpora/stopwords")
except:
    nltk.download("stopwords")

STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def load_motifs(path="motifs.csv"):
    motifs = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            motifs.append({
                "motif": row["motif"],
                "keywords": [k.strip() for k in row["keywords"].split(",")]
            })
    return motifs

def extract_motifs(text, motifs):
    found = set()
    lower = text.lower()
    for m in motifs:
        for k in m["keywords"]:
            if k in lower:
                found.add(m["motif"])
    return list(found)
