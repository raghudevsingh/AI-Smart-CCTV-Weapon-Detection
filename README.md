🛡️ AI Smart CCTV Weapon Detection System

<p align="center">
  <strong>An AI-powered smart surveillance system for intelligent CCTV monitoring and weapon detection.</strong>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/YOLO-Object%20Detection-green" alt="YOLO">
  <img src="https://img.shields.io/badge/Node.js-Backend-green?logo=node.js&logoColor=white" alt="Node.js">
  <img src="https://img.shields.io/badge/Express.js-API-black?logo=express&logoColor=white" alt="Express.js">
  <img src="https://img.shields.io/badge/MongoDB-Database-green?logo=mongodb&logoColor=white" alt="MongoDB">
  <img src="https://img.shields.io/badge/React-Dashboard-blue?logo=react&logoColor=white" alt="React">
</p>---

📌 Overview

The AI Smart CCTV Weapon Detection System is an intelligent surveillance solution designed to analyze CCTV video streams using Artificial Intelligence, Computer Vision, and Deep Learning.

Unlike conventional CCTV systems that primarily record footage for manual review, this project aims to automatically analyze video frames, detect relevant objects such as weapons and people, and preserve evidence of detected incidents.

The system combines an AI-based detection pipeline with backend services, database storage, and a web-based monitoring interface.

---

🎯 Problem Statement

Traditional CCTV surveillance requires continuous human monitoring of multiple camera feeds. This can make identifying critical security incidents difficult and time-consuming.

The objective of this project is to develop an AI-assisted surveillance system capable of:

- Analyzing CCTV / RTSP video streams
- Detecting weapons using object detection
- Detecting people and relevant objects
- Processing video frames automatically
- Capturing evidence of detected incidents
- Storing detection information
- Presenting results through a monitoring dashboard

---

🚀 Key Features

- 🔍 AI-based object detection
- 🔫 Weapon detection
- 👤 Person detection
- 📹 CCTV / RTSP stream processing
- 🧠 Computer Vision-based analysis
- ⚡ Real-time video processing
- 📸 Evidence frame capture
- 🌐 Backend API integration
- 🗄️ Detection data storage
- 📊 Web-based monitoring dashboard

---

🧠 AI & Computer Vision

The AI/ML pipeline is responsible for analyzing incoming video frames and identifying objects relevant to the surveillance system.

Detection Pipeline

flowchart TD
    A["CCTV / RTSP Camera"] --> B["Video Stream"]
    B --> C["OpenCV Processing"]
    C --> D["YOLO Detection Model"]
    D --> E["Object / Weapon Detection"]
    E --> F["Confidence Filtering"]
    F --> G["Evidence Capture"]
    G --> H["Backend API"]
    H --> I["Dashboard / Database"]

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
AI / ML| YOLO, Deep Learning
Computer Vision| OpenCV
Backend| Node.js, Express.js
Database| MongoDB
Frontend| React
Video Input| CCTV / RTSP
Version Control| Git & GitHub

---

📂 Project Structure

AI-Smart-CCTV-Weapon-Detection/
├── backend/
├── frontend/
├── ai/
├── assets/
├── README.md
└── requirements.txt

Components

Component| Purpose
"backend/"| Backend services and APIs
"frontend/"| Web-based monitoring interface
"ai/"| AI/ML and detection components
"assets/"| Images, screenshots and project resources
"README.md"| Project documentation
"requirements.txt"| Python dependencies

«The structure above represents the major project components. Additional files and folders may exist depending on the implementation.»

---

⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/raghudevsingh/AI-Smart-CCTV-Weapon-Detection.git
cd AI-Smart-CCTV-Weapon-Detection

2. Create a Python Virtual Environment

python -m venv venv

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

3. Install Python Dependencies

pip install -r requirements.txt

4. Install Backend Dependencies

cd backend
npm install

5. Configure Environment Variables

Create a ".env" file according to the project configuration.

Example:

PORT=5000
MONGODB_URI=your_mongodb_connection_string

«Never upload passwords, API keys, database credentials, camera credentials, or other sensitive information to GitHub.»

6. Start the Backend

npm start

7. Start the Frontend

cd frontend
npm install
npm start

---

📹 CCTV / RTSP Input

The system can work with different video sources depending on the implementation:

- CCTV cameras
- IP cameras
- RTSP streams
- Local video files
- Test video footage

Example RTSP format:

rtsp://username:password@camera-ip:port/stream

«Do not publish real camera credentials or private RTSP URLs.»

---

🔎 Detection Workflow

The overall processing workflow can be summarized as:

flowchart TD
    A["Video Input"] --> B["Frame Capture"]
    B --> C["OpenCV Processing"]
    C --> D["YOLO Inference"]
    D --> E["Object Detection"]
    E --> F["Confidence Check"]
    F --> G["Evidence Capture"]
    G --> H["Backend Processing"]
    H --> I["Database / Dashboard"]

---

📸 Evidence Capture

When a relevant detection occurs, the system can preserve information such as:

- Detection frame
- Detected object
- Confidence score
- Timestamp
- Associated camera information

This allows detected events to be reviewed after they occur.

---

📊 Monitoring Dashboard

The web dashboard provides a centralized interface for viewing detection-related information.

Depending on the implementation, the dashboard may display:

- Camera feed
- Detection status
- Detected objects
- Confidence scores
- Incident timestamps
- Captured evidence
- Historical detection records

---

🧪 Testing

The system can be tested using:

- Sample images
- Recorded CCTV footage
- Test videos
- Controlled camera streams

Testing can focus on:

- Detection accuracy
- False detections
- Processing speed
- System stability
- Performance under different conditions

---

🔐 Security Considerations

Because the system processes surveillance-related data:

- Keep CCTV credentials private.
- Never commit passwords or API keys.
- Use environment variables for sensitive configuration.
- Restrict access to stored evidence.
- Secure backend APIs before deployment.
- Follow applicable privacy and surveillance regulations.

---

📈 Future Improvements

- 🚨 Real-time alert notifications
- 📱 Mobile push notifications
- 🥊 Fight / violence detection
- 🚪 Unauthorized access detection
- 🎯 Multi-object tracking
- 📹 Improved RTSP stream management
- ☁️ Cloud deployment
- 📊 Advanced analytics
- 🔐 Role-based authentication
- ⚡ AI inference optimization
- 📦 Automated model training and evaluation

---

👨‍💻 Contributors

Prakhar Rai
Project Lead & Project Development

Raghu Dev Singh
Project Development

Nitish Sonkar
Project Development

Ritesh Tiwari
Project Development

---

🎓 Academic Project

This project was developed as a Major Project by students of:

B.Tech — Computer Science & Engineering (AI & ML)

United College of Engineering and Research, Prayagraj
Dr. A.P.J. Abdul Kalam Technical University (AKTU)

---

📚 Learning Outcomes

This project provided practical experience in:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Object Detection
- Video Processing
- Backend API Development
- Database Integration
- Web Application Development
- Git & GitHub
- Team-based Project Development

---

⚠️ Disclaimer

This project is developed for educational and research purposes.

AI-based detection systems can produce false positives and false negatives. The system should therefore be treated as an assistance tool and should not be considered a replacement for professional security personnel or emergency services.

---

⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

🔗 Repository

"AI Smart CCTV Weapon Detection System" (https://github.com/raghudevsingh/AI-Smart-CCTV-Weapon-Detection)
