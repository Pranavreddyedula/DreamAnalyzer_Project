from flask import Flask, request, jsonify, render_template
import torch
import joblib
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import utils, stress

app = Flask(__name__)

# Try loading model
try:
    model = DistilBertForSequenceClassification.from_pretrained('dream_emotion_model')
    mlb = joblib.load('label_encoder.joblib')
    print("Model Loaded Successfully")
except:
    model = None
    mlb = None
    print("Model not found! Using default output")

tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
motifs = utils.load_motifs("motifs.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json.get("text", "")

    cleaned = utils.clean_text(text)
    motifs_found = utils.extract_motifs(text, motifs)

    # Emotion Prediction
    emotions = []
    if model and mlb:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
        with torch.no_grad():
            logits = model(**inputs).logits
        probs = torch.sigmoid(logits).numpy()[0]
        for i, p in enumerate(probs):
            if p >= 0.4:
                emotions.append({"label": mlb.classes_[i], "score": float(p)})
    else:
        emotions.append({"label": "fear", "score": 0.82})

    stress_value = stress.stress_score(text, motifs_found)

    result_report = []
    if "falling" in motifs_found:
        result_report.append("Fear of losing control")
    if stress_value > 60:
        result_report.append("High Stress — Try Relaxation")

    return jsonify({
        "cleaned": cleaned,
        "motifs": motifs_found,
        "emotions": emotions,
        "stress": stress_value,
        "report": result_report
    })

if __name__ == "__main__":
    app.run(debug=True)
