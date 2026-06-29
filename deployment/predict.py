import os
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import (
    load_img,
    img_to_array
)

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

IMAGE_SIZE = 128

# Absolute path to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Absolute path to the model
MODEL_PATH = os.path.join(
    BASE_DIR,
    "Best_Crack_Detection_Model.keras"
)

# ------------------------------------------------------------
# Load Model (Loads only once)
# ------------------------------------------------------------

print("Loading CNN Model...")

model = load_model(MODEL_PATH)

print("Model Loaded Successfully.")

# ------------------------------------------------------------
# Predict Image
# ------------------------------------------------------------

def predict_image(image_path):

    img = load_img(
        image_path,
        target_size=(IMAGE_SIZE, IMAGE_SIZE)
    )

    img_array = img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    prediction = model.predict(
        img_array,
        verbose=0
    )

    prediction_value = float(prediction[0][0])

    if prediction_value < 0.5:

        result = "Crack Detected"
        confidence = (1 - prediction_value) * 100

    else:

        result = "No Crack"
        confidence = prediction_value * 100

    return {
        "class": 0 if prediction_value < 0.5 else 1,
        "prediction": result,
        "confidence": round(confidence, 2),
        "raw_prediction": round(prediction_value, 6)
    }