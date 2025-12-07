from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

try:
    nltk.data.find("sentiment/vader_lexicon")
except:
    nltk.download("vader_lexicon")

sid = SentimentIntensityAnalyzer()

def stress_score(text, motifs_found):
    s = sid.polarity_scores(text)
    neg = s["neg"]
    score = neg * 100

    stress_motifs = {"exam": 15, "chase": 20, "falling": 18, "drowning": 25}
    for m in motifs_found:
        score += stress_motifs.get(m, 0)

    return min(100, round(score))
