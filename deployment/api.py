from fastapi import FastAPI, UploadFile, File
import shutil
import os

from deployment.predict import predict_image

app = FastAPI(
    title="Surface Crack Detection API",
    description="CNN-based Surface Crack Detection",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "Surface Crack Detection API is Running!"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    upload_folder = "uploads"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    image_path = os.path.join(
        upload_folder,
        file.filename
    )

    with open(
        image_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = predict_image(
        image_path
    )

    return result