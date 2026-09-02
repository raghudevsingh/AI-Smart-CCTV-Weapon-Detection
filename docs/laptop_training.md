\# Local Model Training



\## Hardware



\- Laptop: Dell G15

\- GPU: NVIDIA GeForce RTX 3050 Laptop GPU

\- GPU Memory: 6 GB

\- CUDA: 13.0



\## Software Environment



\- Python: 3.11.9

\- Ultralytics: 8.4.124

\- PyTorch: 2.11.0+cu128

\- OpenCV: 5.0.0



\## Project Environment



Virtual environment:



C:\\AI\_CCTV\_Project\\venv



Project directory:



C:\\AI\_CCTV\_Project



\## Dataset



Dataset: Weapon Detection Dataset



Classes:



\- gun

\- knife

\- person



Local dataset:



C:\\AI\_CCTV\_Project\\Weapon\_Detection\_Dataset



\## Model



Model architecture: YOLO11n



The model was trained locally on the Dell G15 laptop using the NVIDIA GeForce RTX 3050 6GB GPU.



\## Training Output



Training directory:



C:\\AI\_CCTV\_Project\\runs\\weapon\_detection\_v1-2



Final model:



C:\\AI\_CCTV\_Project\\runs\\weapon\_detection\_v1-2\\weights\\best.pt



Last checkpoint:



C:\\AI\_CCTV\_Project\\runs\\weapon\_detection\_v1-2\\weights\\last.pt



\## Validation Results



Overall:



\- Precision: 87.7%

\- Recall: 76.6%

\- mAP50: 83.6%

\- mAP50-95: 59.0%



Class-wise results:



| Class | Precision | Recall | mAP50 | mAP50-95 |

|---|---:|---:|---:|---:|

| Gun | 88.1% | 71.6% | 81.0% | 56.6% |

| Knife | 91.4% | 81.3% | 87.7% | 57.5% |

| Person | 83.8% | 77.1% | 82.3% | 62.8% |



\## Live Camera Testing



OpenCV was installed and the laptop webcam was tested successfully.



The trained model was tested using the laptop camera.



A mobile phone was used to display weapon images in front of the webcam.



The model successfully detected gun and knife objects.



The confidence threshold was tested at different values.



A confidence threshold of 0.40 currently provides better practical results than 0.25 during live testing.



\## Model Transfer to Colab



After local training, the trained `best.pt` model was uploaded to Google Drive.



Google Drive/Colab model path:



/content/drive/MyDrive/AI\_CCTV\_Project/weapon\_training/yolo11\_weapon\_v1/weights/best.pt



The model was successfully loaded in Google Colab.



Classes confirmed in Colab:



{0: 'gun', 1: 'knife', 2: 'person'}



\## Next Work



\- Test the model on more unseen images and videos.

\- Analyze false positives and false negatives.

\- Improve live CCTV detection.

\- Add a weapon detection warning.

\- Save evidence frames when a weapon is detected.

\- Develop the final alert/notification feature.

