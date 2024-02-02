import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import StreamingResponse
import cv2
import pickle
import numpy as np
import os
import tensorflow as tf
from dotenv import load_dotenv
from flask import  Flask,render_template,request,jsonify
from fastapi import FastAPI, Request, File, UploadFile,Form

load_dotenv('.env')
 
app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name = "static")
templates = Jinja2Templates(directory="templates")


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


UPLOAD_FOLDER = "images"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.post("/upload_image", response_class=HTMLResponse)
async def upload_image(
    image_file: UploadFile = File(...)
):
    image_path = f"{UPLOAD_FOLDER}/{image_file.filename}"
    save_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    with open(save_path, "wb") as image:
        content = await image_file.read()
        image.write(content)
    process_image(image_path)
      
def process_image(file_path):

    tf.keras.models.load_model('my_model.pkl')
    

    input_image = file_path

    input_image_resized = cv2.resize(input_image, (101, 101))  # Resize to match the model input size
    input_image_rescaled = input_image_resized / 255.0  # Scale pixel values between 0 and 1

    input_image_reshaped = np.expand_dims(input_image_rescaled, axis=0)  # Add batch dimension

    predictions = model.predict(input_image_reshaped).reshape((-1, ))

    binary_predictions = (predictions > 0.5).astype(int)

    # Print or use the predictions as needed
    print("Predictions:", binary_predictions)



if __name__ == '__main__':
   uvicorn.run(app, host='0.0.0.0', port=8000)