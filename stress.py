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
    score = neg * 100  # base using negative sentiment

    # Updated weights for more accurate stress detection
    stress_motifs = {
        "exam": 20,
        "chase": 25,
        "falling": 18,
        "drowning": 30,
        "dark": 10,
        "monster": 15
    }

    for m in motifs_found:
        score += stress_motifs.get(m, 0)

    return min(100, round(score))
