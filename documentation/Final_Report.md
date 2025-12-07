# AI-Based Dream Analyzer using NLP & Deep Learning  
**Major Project | B.Tech CSE | Tirumala Engineering College – JNTUK**  
**Batch: 2022–2026**  

---

## 💡 Abstract
Dreams reflect our subconscious emotions such as fear, anxiety, joy, or stress.  
This project uses **Artificial Intelligence (AI)** and **Natural Language Processing (NLP)** to analyze a user’s dream text and identify:

- Emotion Labels (multi-label classification)
- Dream Motifs (symbolic patterns)
- Stress Level Score (0–100)
- Meaningful Summary/Insights

The system is implemented as a lightweight **Flask web application** with a **dark theme UI**.

---

## 📘 Chapter 1 — Introduction
Dreams are symbolic expressions of suppressed thoughts, stress and imagination.  
Manual interpretation is difficult and subjective.

### Objectives
- Clean and process dream text using NLP
- Predict emotional state using Deep Learning
- Extract meaningful motifs from dreams
- Calculate a stress score using sentiment
- Display user-friendly results in browser

### Scope
- Analyses only **written dream text**
- Not a replacement for psychology or medical diagnosis

---

## 📘 Chapter 2 — Literature Survey
- **Freud & Jung**: Dreams represent unconscious desires and symbols
- **Sentiment Analysis**: Detects emotional polarity
- **Transformers** (BERT/DistilBERT): State-of-the-art textual understanding
- **Existing apps**: Lack dream-focused emotion + motif + stress analysis

GAP: No existing software combines **all three**:
➡ Emotion + Motif + Stress

---

## 📘 Chapter 3 — System Analysis & Design

### 🏗 Architecture
```text
Frontend UI → Flask API → Emotion Model → Motif Engine → Stress Analyzer → Dashboard
User → Dream Analyzer → Results
Input → NLP → Emotion Model → Motifs → Stress → Output Display
USER (1) → (M) DREAMS (1) → (1) ANALYSIS
Chapter 4 — Implementation
Tech Stack
Component	Technology
Language	Python
Backend	Flask
NLP Model	DistilBERT
Sentiment	NLTK VADER
Frontend	HTML + Bootstrap Dark
Storage	CSV / Local Data
Algorithm

1️⃣ Preprocess Dream Text
2️⃣ Emotion Classification (Multi-label)
3️⃣ Keyword-based Motif Extraction
4️⃣ Stress Scoring (sentiment + motif weight)
5️⃣ Results Display in Web UI
Chapter 5 — Results

Example Input:

"I was falling from a tall building and a monster was chasing me."

Output Type	Result
Motifs	falling, chase
Emotions	fear(0.92), anxiety(0.80)
Stress Score	88 / 100
Insights	Fear of losing control, High stress
Results are displayed instantly on the dashboard.
Graphs of motif frequency, stress trend, and emotional distribution can be added for UI enhancement.
Chapter 6 — Conclusion & Future Work
Conclusion

The system successfully:

Analyzes dream text using NLP & AI

Identifies emotional patterns and stress

Extracts meaningful motifs linked to subconscious mind

Future Enhancements

Mobile App

Voice input support

Richer labeled dataset for higher accuracy

Personalized recommendations

Cloud storage & user history analysis

📚 References

Hugging Face – Transformers Documentation

NLTK VADER Lexicon

Dream psychology research articles

University standard project references

🧑‍🎓 Project Details
Field	Information
Student	Edula Sai Pranav Reddy
Roll No	23NE5A0502
Guide	Dr. K. Satish
College	Tirumala Engineering College
Department	Computer Science & Engineering
