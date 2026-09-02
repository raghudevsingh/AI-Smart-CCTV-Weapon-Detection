\# AI Smart CCTV – Weapon Detection System



\## Project Overview



AI Smart CCTV is a computer vision-based security system designed to detect potentially dangerous objects such as guns and knives using a YOLO object detection model.



The project uses YOLO11n and a custom Weapon Detection Dataset containing three classes:



\- Gun

\- Knife

\- Person



The model was trained locally on a Dell G15 laptop using an NVIDIA GeForce RTX 3050 6GB Laptop GPU.



\## Objectives



\- Detect weapons automatically from images and live camera input.

\- Identify guns and knives using object detection.

\- Reduce the need for continuous manual CCTV monitoring.

\- Provide a foundation for real-time security alerts.

\- Create a system that can later be extended to notifications and evidence capture.



\## Technology Stack



\- Python 3.11.9

\- YOLO11n

\- Ultralytics 8.4.124

\- PyTorch 2.11.0+cu128

\- OpenCV 5.0.0

\- NVIDIA GeForce RTX 3050 6GB

\- Google Colab

\- GitHub



\## Dataset



The project uses a Weapon Detection Dataset with the following classes:



| Class | Description |

|---|---|

| 0 | Gun |

| 1 | Knife |

| 2 | Person |



The dataset contains separate training, validation, and testing sets.



The complete dataset is not included in this repository because of its large size.



\## Model Training



The YOLO11n model was trained locally on a Dell G15 laptop using the NVIDIA RTX 3050 GPU.



Training output was generated using Ultralytics and includes:



\- Precision and recall curves

\- F1 curve

\- Precision-Recall curve

\- Confusion matrix

\- Training/validation results

\- Validation predictions



The trained model is stored in:



```text

model/best.pt

