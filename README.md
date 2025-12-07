# DreamAnalyzer_Project
# 🌙 AI Dream Analyzer – Final Year Major Project (CSE)

[![Live Demo](https://img.shields.io/badge/Website-LIVE-success?style=for-the-badge)](https://dreamanalyzer-project.onrender.com)
[![GitHub Repo](https://img.shields.io/badge/View_Code-GitHub-black?style=for-the-badge)](https://github.com/Pranavreddyedula/DreamAnalyzer_Project)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-orange?style=flat-square)
![NLP](https://img.shields.io/badge/NLP-Text_Analysis-yellow?style=flat-square)
![Render](https://img.shields.io/badge/Hosting-Render-purple?style=flat-square)

> A simple AI-powered web app that analyzes dreams, detects hidden emotions, stress level,
> and psychological motifs using NLP.

---

## 🧠 Project Overview

Dreams often carry psychological meaning — fear, stress, happiness, trauma etc.  
This project uses **Natural Language Processing** to analyze dream text and provide:

✔ **Emotion Prediction**  
✔ **Stress Score (0–100)**  
✔ **Motif Detection** (falling, chase, drowning, darkness, exam etc.)  
✔ **Psychological Interpretation**

---

## 🚀 Live Website  
👉 https://dreamanalyzer-project.onrender.com  
(Type any dream & click **Analyze** to see output)

---

## 📌 Features

| Feature | Description |
|--------|-------------|
| 🧠 Emotion Analysis | Identifies fear, anxiety, joy, neutral states |
| 🚨 Stress Detection | Calculates stress score based on text & motifs |
| 🔍 Dream Motif Engine | Detects themes like falling, chase, drowning… |
| 🧹 Text Preprocessing | Cleaning & NLP pipeline |
| 🌐 Cloud Deployment | Hosted online using Render |
| ✨ Fast UI | Built with Flask + Bootstrap |

---

## 🏗️ System Architecture

User Dream Text → NLP Processing → Sentiment Model → Motif Engine → Stress Score → JSON Result

yaml
Copy code

📌 (Poster contains full architecture diagram)

---

## 🖥️ Screenshots
<img width="707" height="429" alt="Screenshot 2025-12-07 113832" src="https://github.com/user-attachments/assets/06050770-cf2a-4ccf-abf6-7366375ffa9d" />
<img width="703" height="416" alt="Screenshot 2025-12-07 113853" src="https://github.com/user-attachments/assets/4ee83206-551b-4eb5-8e63-74d13c4df2b4" />
<img width="1656" height="820" alt="Screenshot 2025-12-07 114001" src="https://github.com/user-attachments/assets/b8a3a9db-040a-4e6f-a04e-8ff2388e02de" />

## 🛠️ Tech Stack![Uploading Screenshot 2025-12-07 114001.png…]()
| Category | Technology |
|---------|------------|
| Backend | Python Flask |
| NLP | NLTK (VADER) |
| Frontend | HTML, CSS, Bootstrap |
| Hosting | Render.com |
| Dataset | Custom motifs & sample dreams |

---

## 📂 Project Structure

DreamAnalyzer_Project/
│
├── app.py # Flask backend
├── utils.py # Text cleaning + motif extraction
├── stress.py # Stress score model
├── requirements.txt # Dependencies
│
├── templates/
│ └── index.html # UI
│
├── motifs.csv # Motif keywords
├── dreams_sample.csv # Demo dreams
└── documentation/
├── Final_Report.pdf
├── Poster.pdf
└── Presentation.pptx

yaml
Copy code

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/Pranavreddyedula/DreamAnalyzer_Project
cd DreamAnalyzer_Project
pip install -r requirements.txt
python app.py
Open browser → http://127.0.0.1:5000/

📊 Sample Output JSON
css
Copy code
{
 "cleaned": "i was falling from a tall building and a monster was chasing me in the dark",
 "emotions": [{"label": "fear/anxiety", "score": 0.82}],
 "motifs": ["falling", "chase", "dark", "monster"],
 "stress": 85,
 "report": [
   "Loss of control or fear of failure.",
   "High stress indicators detected."
 ]
}
🧩 Future Enhancements
✔ Deep-learning model for emotion detection
✔ Add user login & dream history
✔ More motifs + larger dataset
✔ Visualization of dream trend over time

👨‍💻 Developer
Edula Sai Pranav Reddy
✉️ Open to work in: AI / NLP / Web Development
🎓 Tirumala Engineering College – CSE (2022–2026)

❓ Viva Questions (Quick Revision)
Question	What to Answer
What is NLP?	NLP = allowing computers to understand human language
Why VADER?	Lightweight sentiment model for short expressions
Why Flask?	Easy deployment of small web apps
What is a motif?	Recurring theme indicating psychological state
How stress score is calculated?	Negative sentiment + weighted motifs
Deployment?	Cloud hosting on Render
Dataset?	Custom labeled dreams & motifs

⭐ Thanks for Visiting!
If you like this project, please ⭐ the repo!
