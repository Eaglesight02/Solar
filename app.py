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
from dotenv import load_dotenv

from flask import  Flask,render_template,request,jsonify
from fastapi import FastAPI, File, UploadFile, Request
load_dotenv('.env')
 
app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name = "static")
templates = Jinja2Templates(directory="templates")

UPLOAD_FOLDER = "uploads"
app.mount("/static", app=StaticFiles(directory="static"), name="static")

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/process_image")
async def process_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as image:
        shutil.copyfileobj(file.file, image)

    result = your_image_processing_function(file_path)

    return {"result": result}

def your_image_processing_function(file_path):
    # Implement your image processing logic here
    # Example: You can use a library like OpenCV to process the image
    # For simplicity, let's just return the file path in this example
    return f"Image processed successfully. Path: {file_path}"

if __name__ == '__main__':
   uvicorn.run(app, host='0.0.0.0', port=8000)