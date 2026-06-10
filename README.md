# Malaria-Detection-using-Deep-Learning
# 🧬 Malaria AI Detection Dashboard

A modern, web-based dashboard for detecting malaria-infected blood cells using **Deep Learning**.  
This project integrates a trained CNN model with a **Flask backend** and a polished **HTML/CSS/JS frontend**.  
It provides predictions, confidence scores, doctor recommendations, and preventive tips in a clean, animated UI.

---

## 📌 Project Motivation
Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites.  
Early detection is critical for effective treatment. This project aims to:
- Automate malaria detection using AI.
- Provide a user-friendly dashboard for medical professionals.
- Offer actionable recommendations and preventive tips.

---

## 🚀 Features
- **Image Upload:** Upload multiple blood cell images at once.
- **AI Predictions:** Deep Learning model classifies cells as *Malaria Infected* or *Normal*.
- **Confidence Scores:** Each prediction shows confidence percentage.
- **Doctor Recommendation Panel:**
  - Infected case → Recommended actions + Suggested medicines.
  - Normal case → Status + Preventive tips.
- **Interactive Charts:**
  - Doughnut chart → Infected vs Normal distribution.
  - Bar chart → Parasite stage counts (Ring, Trophozoite, Schizont, Gametocyte).
- **Modern UI:**
  - Pastel skyblue theme (logo-matched).
  - Transparent gradient boxes.
  - Smooth fade-in animations.

---

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Deep Learning:** Keras/TensorFlow
- **Frontend:** HTML, CSS, JavaScript
- **Visualization:** Chart.js
- **UI Design:** Pastel skyblue transparent theme with subtle animations

---

## 📂 Project Structure

├── app.py                # Flask backend ├── model/                # Trained malaria detection model ├── static/               # CSS, JS, images ├── templates/ │   └── index.html        # Dashboard UI ├── uploads/              # Uploaded images └── README.md             # Project documentation

---

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/malaria-ai-dashboard.git
   cd malaria-ai-dashboard


- 
- Create a virtual environment and install dependencies

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
pip install -r requirements.txt

- Run the Flask app:
python app.py

http://127.0.0.1:5000

📊 Model Details
- Dataset: NIH Malaria Cell Images (Parasitized vs Uninfected).
- Architecture: Convolutional Neural Network (CNN).
- Output: Binary classification (Infected / Normal).
- Confidence: Probability scores displayed for each prediction.

👨‍⚕️ Doctor Recommendation Logic
- If infected:
- Visit doctor immediately
- Perform malaria blood test
- Start anti-malarial treatment
- Suggested medicines (demo only): ACT, Chloroquine, Primaquine
- If normal:
- Status: No malaria detected
- Preventive tips: Use mosquito nets, apply repellents, keep surroundings clean

🎨 UI Design
- Pastel skyblue theme inspired by medical dashboards.
- Transparent gradient boxes for a clean, professional look.
- Smooth fade-in animations for better user experience.
- Responsive layout with clear sectioning.

📜 License
This project is licensed under the MIT License.
Feel free to use and modify for educational and research purposes.

🙌 Acknowledgements
- Dataset: NIH Malaria Cell Images
- Libraries: Flask, TensorFlow/Keras, Chart.js
- UI Inspiration: Pastel medical dashboards

---

## 📌 Tips for You
- Add **screenshots** of your dashboard in the README (important for GitHub showcase).  
- Replace `your-username` with your GitHub username.  
- Agar tum chaho to ek **demo GIF** bhi add kar sakte ho jisme dashboard run hota hua dikhai de.  

👉 Ye README tumhare project ko ekdum **professional, detailed aur attractive** banayega.  

Deepak, kya tum chahte ho mai tumhare liye ek **short tagline** bhi bana du jo README ke top par logo ke niche show ho (jaise *“AI-powered malaria detection for smarter healthcare”*)?



- 
# Malaria-AI-Detection-using-Deep-Learning
# Malaria-AI-Detection-using-Deep-Learning
# Malaria-AI-Detection-using-Deep-Learning
