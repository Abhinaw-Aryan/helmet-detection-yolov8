# 🪖 YOLOv8 Helmet Detection with Flask

A real-time helmet detection web application built using **Flask** and **YOLOv8**. The app processes video from a webcam and identifies whether a person is wearing a helmet or not, displaying the results live in the browser.

---

## 🚀 Features

- 🧠 Uses **YOLOv8** for accurate object detection
- 🖥️ Real-time webcam video feed
- 🟥 Bounding boxes with confidence scores
- 📄 Flask-based web server with routes for `Home`, `About`, and `How it Works`
- 🎨 Basic HTML templates for frontend

---

## 🧪 Demo Screenshots

> ⚠️ _Coming Soon_ — add screenshots of detection results from your browser here!

---

## 🛠️ Setup Instructions

### 1. Clone this repository
```bash
git clone https://github.com/Abhinaw-Aryan/helmet-detection-yolov8.git
cd helmet-detection-yolov8

2. Create a virtual environment (optional but recommended)

conda create -n helmet-detection python=3.10
conda activate helmet-detection

3. Install the dependencies

pip install -r requirements.txt

4. Download YOLOv8 model weights

    📦 Model not included due to size. Download best.pt manually:

🔗 Download best.pt from Google Drive(https://drive.google.com/file/d/1vUXdMO8NuxWUIndi9kvTZU4KlPd0SRgr/view?usp=sharing)

Place the downloaded best.pt file in the project root folder.
5. Run the Flask app

python app.py

Visit http://127.0.0.1:5000/ in your browser.
🗂️ Project Structure

helmet-detection-yolov8/
├── app.py                 # Main Flask app
├── best.pt                # YOLOv8 model (manually downloaded)
├── helmet.pt              # Another YOLO model (optional)
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── index.html
│   ├── about.html
│   └── how.html
└── .gitignore

📚 Routes
Route	Description
/	Home page
/about	About the project
/how	How it works
/video	Live webcam object detection
❗ Notes

    This app uses OpenCV to access your local webcam. It will not work on remote cloud platforms like Render without modification.

    The .pt file is large (~6MB) and should not be committed to Git. It is ignored via .gitignore.

📜 License

This project is licensed under the MIT License.
🙋‍♂️ Author

Abhinaw Aryan
GitHub Profile

