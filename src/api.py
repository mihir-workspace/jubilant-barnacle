import os
import cv2
import fastapi
from fastapi import File, UploadFile, File
import shutil

current_path = os.getcwd()
temp_path = os.path.join(current_path,'temp')

endpoints = fastapi.FastAPI()

@endpoints.post("/extractor")
def from_info_extractor(file:UploadFile=File(...)):

    file_savePath =  os.path.join(temp_path,file.filename)

    with open(file_savePath,'wb') as f:
        shutil.copyfileobj(file.file, f)

    return {
        "Message":"File is saved successfully",
        "data":file.filename
    }

@endpoints.get("/")
def ping():

    data = {
        "Message_code":200,
        "Message":"Alive"
    }

    return data


