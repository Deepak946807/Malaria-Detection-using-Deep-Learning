from flask import Flask, render_template, request
import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename

app = Flask(__name__)
model = load_model("model.h5")

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    infected = 0
    normal = 0
    parasite_counts = {"Ring": 0, "Trophozoite": 0, "Schizont": 0, "Gametocyte": 0}
    error_msg = None

    if request.method == "POST":
        files = request.files.getlist("images")

        for file in files:
            if not allowed_file(file.filename):
                error_msg = "❌ Sirf PNG/JPG images allowed hain!"
                continue

            filename = secure_filename(file.filename)
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path)

            img = cv2.imread(path)
            if img is None:
                results.append({
                    "image": path,
                    "label": "⚠️ Invalid Image",
                    "confidence": 0,
                    "is_invalid": True
                })
                continue

            # Preprocess
            img_resized = cv2.resize(img, (64, 64))
            img_normalized = img_resized / 255.0
            img_input = np.reshape(img_normalized, (1, 64, 64, 3))

            preds = model.predict(img_input)[0]

            # Terminal mein class indices dekho
            # {'Other': 0, 'Parasitized': 1, 'Uninfected': 2}
            other_prob    = float(preds[0])
            infected_prob = float(preds[1])
            normal_prob   = float(preds[2])

            predicted_class = np.argmax(preds)

            # Class 0 = Other = Invalid
            if predicted_class == 0:
                results.append({
                    "image": path,
                    "label": "⚠️ Invalid Image",
                    "confidence": round(other_prob * 100, 2),
                    "is_invalid": True
                })
                continue

            # Class 1 = Parasitized = Infected
            elif predicted_class == 1:
                label = "Malaria Infected"
                confidence = round(infected_prob * 100, 2)
                infected += 1
                if confidence > 90:
                    parasite_counts["Ring"] += 2
                    parasite_counts["Trophozoite"] += 1
                elif confidence > 75:
                    parasite_counts["Trophozoite"] += 2
                    parasite_counts["Schizont"] += 1
                else:
                    parasite_counts["Schizont"] += 1
                    parasite_counts["Gametocyte"] += 1

            # Class 2 = Uninfected = Normal
            else:
                label = "Normal Cell"
                confidence = round(normal_prob * 100, 2)
                normal += 1

            results.append({
                "image": path,
                "label": label,
                "confidence": confidence,
                "is_invalid": False
            })

    total_parasites = sum(parasite_counts.values())
    return render_template(
        "index.html",
        results=results,
        infected=infected,
        normal=normal,
        parasite_counts=parasite_counts,
        total_parasites=total_parasites,
        error_msg=error_msg
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)