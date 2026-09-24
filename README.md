🛡️ AI Smart CCTV Weapon Detection System

«An AI-powered smart surveillance system for detecting weapons and suspicious activities from CCTV video streams using Computer Vision and Deep Learning.»

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv&logoColor=white" alt="OpenCV"/>
  <img src="https://img.shields.io/badge/YOLO-Object%20Detection-green" alt="YOLO"/>
  <img src="https://img.shields.io/badge/Node.js-Backend-green?logo=node.js&logoColor=white" alt="Node.js"/>
  <img src="https://img.shields.io/badge/Express.js-API-black?logo=express&logoColor=white" alt="Express.js"/>
  <img src="https://img.shields.io/badge/MongoDB-Database-green?logo=mongodb&logoColor=white" alt="MongoDB"/>
  <img src="https://img.shields.io/badge/React-Dashboard-blue?logo=react&logoColor=white" alt="React"/>
</p>---

📌 Overview

Traditional CCTV systems mainly record video footage and depend on continuous human monitoring. Monitoring multiple camera feeds manually can make it difficult to identify critical incidents quickly.

The AI Smart CCTV Weapon Detection System uses Artificial Intelligence and Computer Vision to analyze CCTV footage and identify potentially dangerous objects or suspicious activities.

The system is designed to assist security personnel by automatically analyzing video streams, detecting relevant objects, and preserving evidence for later review.

---

🎯 Problem Statement

Conventional CCTV surveillance relies heavily on human observation. Continuous monitoring of multiple camera feeds can be challenging and may result in delayed identification of security incidents.

This project aims to develop an intelligent surveillance solution that can:

- Automatically analyze CCTV video streams
- Detect weapons using AI-based object detection
- Identify people and relevant objects
- Capture evidence of detected incidents
- Provide detection information through a centralized system

---

🚀 Key Features

- 🔍 AI-based object detection
- 📹 CCTV / RTSP video stream processing
- 🔫 Weapon detection
- 👤 Person detection
- 🧠 Computer Vision-based analysis
- 📸 Automatic evidence capture
- ⚡ Real-time video processing
- 🌐 Backend API integration
- 📊 Web-based monitoring dashboard
- 🗄️ Detection data storage

---

🧠 AI & Computer Vision

The AI/ML component forms the core of the surveillance system.

Detection Pipeline

+----------------------+
| CCTV / RTSP Camera   |
+----------+-----------+
           |
           v
+----------------------+
| Video Stream         |
| Processing (OpenCV)  |
+----------+-----------+
           |
           v
+----------------------+
| YOLO Detection Model |
+----------+-----------+
           |
           v
+----------------------+
| Object / Weapon      |
| Detection            |
+----------+-----------+
           |
           v
+----------------------+
| Confidence Filtering |
+----------+-----------+
           |
           v
+----------------------+
| Evidence Capture     |
+----------+-----------+
           |
           v
+----------------------+
| Backend API          |
+----------+-----------+
           |
           v
+----------------------+
| Dashboard / Database |
+----------------------+

AI/ML Technologies

- Python
- OpenCV
- YOLO
- Computer Vision
- Deep Learning
- Object Detection

---

🏗️ System Architecture

                         +----------------------+
                         |   CCTV / IP Camera   |
                         |      RTSP Stream     |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |   Video Processing   |
                         |        OpenCV        |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |   YOLO Detection     |
                         |        Model         |
                         +----------+-----------+
                                    |
                       +------------+------------+
                       |                         |
                       v                         v
              +----------------+       +----------------+
              | Object         |       | Incident       |
              | Detection      |       | Detection      |
              +--------+-------+       +--------+-------+
                       |                         |
                       +------------+------------+
                                    |
                                    v
                         +----------------------+
                         | Evidence / Results   |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         | Node.js + Express.js |
                         |       Backend        |
                         +----------+-----------+
                                    |
                       +------------+------------+
                       |                         |
                       v                         v
              +----------------+       +----------------+
              |    MongoDB     |       | React          |
              |    Database    |       | Dashboard      |
              +----------------+       +----------------+

---

🛠️ Technology Stack

Category| Technologies
Programming| Python, JavaScript
Computer Vision| OpenCV
AI / ML| YOLO, Deep Learning
Backend| Node.js, Express.js
Database| MongoDB
Frontend| React
Video Input| CCTV / RTSP
Version Control| Git & GitHub

---

📂 Project Structure

AI-Smart-CCTV-Weapon-Detection/
│
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   └── server.js
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── ai/
│   ├── models/
│   ├── detection/
│   └── scripts/
│
├── assets/
│   └── screenshots/
│
├── README.md
└── requirements.txt

«Update the structure above if the repository uses different folder names.»

---

⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/raghudevsingh/AI-Smart-CCTV-Weapon-Detection.git
cd AI-Smart-CCTV-Weapon-Detection

2. Create a Python Virtual Environment

python -m venv venv

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

3. Install Python Dependencies

pip install -r requirements.txt

4. Install Backend Dependencies

cd backend
npm install

5. Configure Environment Variables

Create a ".env" file according to the backend configuration.

Example:

PORT=5000
MONGODB_URI=your_mongodb_connection_string

«Never commit API keys, passwords, database credentials, or other secrets to GitHub.»

6. Start the Backend

npm start

7. Start the Frontend

cd frontend
npm install
npm start

---

📹 CCTV / RTSP Input

The system can process video from sources such as:

- CCTV cameras
- IP cameras
- RTSP streams
- Local video files
- Test video footage

Example RTSP format:

rtsp://username:password@camera-ip:port/stream

«Never publish real camera credentials or private RTSP URLs.»

---

🔎 Detection Workflow

The system follows the following workflow:

Video Input
     ↓
Frame Capture
     ↓
OpenCV Processing
     ↓
YOLO Inference
     ↓
Object Detection
     ↓
Confidence Check
     ↓
Evidence Capture
     ↓
Backend Processing
     ↓
Database / Dashboard

---

📸 Evidence Capture

When a relevant detection occurs, the system can preserve information such as:

- Detection frame
- Timestamp
- Detected object
- Confidence score
- Associated camera information

This helps security personnel review detected incidents.

---

📊 Monitoring Dashboard

The web dashboard provides a centralized interface for monitoring detection results.

Depending on the implementation, the dashboard can display:

- Live or processed camera feed
- Detection status
- Detected objects
- Confidence scores
- Incident timestamps
- Captured evidence
- Historical detection records

---

🧪 Testing

The detection pipeline can be tested using:

- Sample images
- Recorded CCTV footage
- Test videos
- Controlled camera streams

Testing can evaluate:

- Detection accuracy
- False detections
- Processing speed
- System stability
- Performance under different conditions

---

🔐 Security Considerations

Because this project deals with surveillance data:

- Do not expose private CCTV streams.
- Do not commit passwords or API keys.
- Store sensitive credentials using environment variables.
- Restrict access to stored evidence.
- Secure backend APIs before deployment.
- Follow applicable privacy and surveillance regulations.
- Treat AI detection as an assistance mechanism rather than a sole basis for security decisions.

---

📈 Future Improvements

- 🚨 Real-time alert notifications
- 📱 Mobile push notifications
- 🥊 Fight / violence detection
- 🚪 Unauthorized access detection
- 🎯 Multi-object tracking
- 📹 Improved RTSP stream management
- ☁️ Cloud deployment
- 📊 Advanced analytics dashboard
- 🔐 Role-based authentication
- ⚡ AI inference optimization
- 📦 Automated model training and evaluation

---

👨‍💻 Contributors

Name| Role
Prakhar Rai| Project Lead & Project Development
Raghu Dev Singh| Project Development
Nitish Sonkar| Project Development
Ritesh Tiwari| Project Development

---

🎓 Academic Project

This project was developed as a Major Project by students of:

B.Tech — Computer Science & Engineering (AI & ML)
United College of Engineering and Research, Prayagraj
Dr. A.P.J. Abdul Kalam Technical University (AKTU)

---

📚 Learning Outcomes

Through this project, we worked with:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Object Detection
- Video Processing
- Backend API Development
- Database Integration
- Web Dashboard Development
- Git & GitHub
- Team-based Software Development

---

⚠️ Disclaimer

This project is developed for educational and research purposes.

AI-based detection systems may produce false positives or false negatives and should not be considered a replacement for professional security personnel or emergency services.

---

⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

🔗 Repository

"AI Smart CCTV Weapon Detection System" (https://github.com/raghudevsingh/AI-Smart-CCTV-Weapon-Detection)
