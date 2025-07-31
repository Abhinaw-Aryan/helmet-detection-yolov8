from flask import Flask, render_template, Response
from ultralytics import YOLO
import cv2
import atexit

app = Flask(__name__)
model = YOLO("C:\\Users\\KIIT\\Desktop\\TATA\\helmet-detection-flask\\best.pt")
cap = cv2.VideoCapture(0)

@atexit.register
def cleanup():
    cap.release()

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        results = model(frame)[0]
        for idx, box in enumerate(results.boxes):
            conf = float(box.conf[0].item())
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = f"{'No Helmet' if idx == 0 else 'Helmet'} {conf:.2f}"
            color = (0, 0, 255) if idx == 0 else (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, max(y1 - 10, 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/how')
def how():
    return render_template('how.html')

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
