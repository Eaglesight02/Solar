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
from main import management,check,gen_frames,updatedValues1,updatedValues2


from flask import  Flask,render_template,request,jsonify

from chat import get_response

load_dotenv('.env')
 
app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name = "static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("open.html", {"request": request})


if __name__ == '__main__':
   uvicorn.run(app, host='0.0.0.0', port=8000)