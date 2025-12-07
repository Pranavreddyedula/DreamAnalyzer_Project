from flask import Flask, request, jsonify, render_template
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import utils, stress

# Ensure VADER lexicon is available
try:
    nltk.data.find("sentiment/vader_lexicon")
except:
    nltk.download("vader_lexicon")

app = Flask(__name__)
sid = SentimentIntensityAnalyzer()
motifs = utils.load_motifs("motifs.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json or {}
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "Empty text"}), 400

    cleaned = utils.clean_text(text)
    motifs_found = utils.extract_motifs(text, motifs)

    scores = sid.polarity_scores(text)
    neg = scores["neg"]
    pos = scores["pos"]
    neu = scores["neu"]

    # Improved emotion detection logic
    emotions = []
    if neg >= 0.1 or scores["compound"] < 0:
        emotions.append({"label": "fear/anxiety", "score": float(max(neg, 0.4))})
    if pos >= 0.3:
        emotions.append({"label": "joy/positive", "score": float(pos)})
    if not emotions and neu >= 0.5:
        emotions.append({"label": "neutral", "score": float(neu)})
    if not emotions:
        emotions.append({"label": "uncertain", "score": float(neu)})

    stress_value = stress.stress_score(text, motifs_found)

    interpretation = []
    if "falling" in motifs_found:
        interpretation.append("Loss of control or fear of failure.")
    if "exam" in motifs_found:
        interpretation.append("High performance stress.")
    if stress_value > 60:
        interpretation.append("High stress indicators detected.")
    if not interpretation:
        interpretation.append("Dream appears normal with no strong signals.")

    return jsonify({
        "cleaned": cleaned,
        "motifs": motifs_found,
        "sentiment_scores": scores,
        "emotions": emotions,
        "stress": stress_value,
        "report": interpretation
    })

if __name__ == "__main__":
    app.run(debug=True)
