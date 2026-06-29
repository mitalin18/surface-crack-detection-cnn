# Surface Crack Detection using Convolutional Neural Networks (CNN)

A deep learning-based web application for automated surface crack detection using Convolutional Neural Networks (CNN). The project includes model training, experiment tracking with MLflow, REST API deployment using FastAPI, and containerization using Docker.

---

## Project Overview

Surface crack detection plays an important role in structural health monitoring and quality inspection. Manual inspection is time-consuming, subjective, and prone to human error.

This project automates the crack detection process by training a CNN model capable of classifying images into:

* Crack
* No Crack

The trained model is deployed as a REST API using FastAPI and containerized with Docker for easy deployment.

---

#  Features

* CNN-based binary image classification
* Image preprocessing pipeline
* Model training and evaluation
* TensorBoard integration
* MLflow experiment tracking
* Single image prediction
* REST API using FastAPI
* Interactive Swagger UI
* Dockerized deployment
* Modular project structure

---

#  Project Structure

Surface Crack Detection using CNN/
│
├── training/
│   ├── CNN_Surface_Crack_Detection.py
│   ├── mlflow_utils.py
│   ├── CrackDataset/
│   └── Processed_CrackDataset/
│
├── deployment/
│   ├── __init__.py
│   ├── api.py
│   ├── predict.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── Best_Crack_Detection_Model.keras
│
└── .dockerignore
```

---

# Model Architecture

The CNN consists of four convolutional blocks followed by fully connected layers.

```
Input Image (128 × 128 × 3)
↓
Conv2D
↓
Batch Normalization
↓
MaxPooling
↓
Conv2D
↓
Batch Normalization
↓
MaxPooling
↓
Conv2D
↓
Batch Normalization
↓
MaxPooling
↓
Conv2D
↓
Batch Normalization
↓
MaxPooling
↓
Flatten
↓
Dense
↓
Dropout
↓
Dense
↓
Dropout
↓
Dense (Sigmoid)
```

---

# Dataset

Dataset Classes:

* Crack
* No Crack

Images are resized to:

```
128 × 128 × 3
```

Dataset split:

* Training
* Validation
* Testing

---

# Training Pipeline

The training workflow consists of:

1. Dataset preprocessing
2. Image normalization
3. CNN model creation
4. Model compilation
5. Model training
6. Model evaluation
7. TensorBoard logging
8. MLflow experiment tracking
9. Model saving

---

## Experiment Tracking

The project integrates **MLflow** for experiment tracking and **TensorBoard** for visualizing training progress.

### MLflow

Launch the MLflow Tracking UI:

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

MLflow logs:

* Parameters
* Training Accuracy
* Validation Accuracy
* Loss
* Precision
* Recall
* AUC
* Saved Model

---

### TensorBoard

Launch TensorBoard:

```bash
tensorboard --logdir logs
```

Open:

```text
http://localhost:6006
```

Run the training script in a separate terminal while TensorBoard is running to monitor training metrics in real time.

---

# FastAPI Deployment

The trained model is served using FastAPI.

Available endpoints:

### Home

```
GET /
```

Returns API status.

---

### Predict

```
POST /predict
```

Accepts an image file and returns the prediction.

Example Response:

```json
{
    "class": 0,
    "prediction": "Crack Detected",
    "confidence": 99.48,
    "raw_prediction": 0.005233
}
```

---

#  Docker Deployment

Build Docker Image

```bash
docker build -f deployment/Dockerfile -t surface-crack-api .
```

Run Docker Container

```bash
docker run -p 8000:8000 surface-crack-api
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

#  Technologies Used

### Programming Language

* Python

### Deep Learning

* TensorFlow
* Keras

### Image Processing

* OpenCV
* Pillow
* NumPy

### Backend

* FastAPI
* Uvicorn

### Experiment Tracking

* MLflow
* TensorBoard

### Deployment

* Docker

---

# Model Output

The model predicts one of the following classes:

| Prediction     | Description               |
| -------------- | ------------------------- |
| Crack Detected | Surface crack identified  |
| No Crack       | No surface crack detected |

The API also returns:

* Prediction Confidence
* Raw Prediction Score

---

#  Running the Project

## 1. Clone Repository

```bash
git clone <repository-url>
```

---

## 2. Install Dependencies

### Training Environment

Install the dependencies required for model training:

```bash
pip install -r training/requirements.txt
```

### Deployment Environment

Install the dependencies required for running the FastAPI application:

```bash
pip install -r deployment/requirements.txt
```

---

## 3. Start FastAPI

```bash
uvicorn deployment.api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 4. Docker

Build

```bash
docker build -f deployment/Dockerfile -t surface-crack-api .
```

Run

```bash
docker run -p 8000:8000 surface-crack-api
```

---

# Future Improvements

* Improve model accuracy through hyperparameter tuning
* Implement Grad-CAM for model explainability
* Cloud deployment (Azure App Service / AWS / Render)
* CI/CD using GitHub Actions
* Model versioning and registry using MLflow
* User authentication for API
* Web interface for image upload

---

# License

This project is intended for educational and research purposes.

---

# Author

**Mitali Nilapwar**

