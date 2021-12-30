import os
import cv2
import fastapi
from fastapi import File, UploadFile, File
import shutil
from handwritten import OCRExtractor

current_path = os.getcwd()
temp_path = os.path.join(current_path,'temp')
ocr_extractor = OCRExtractor(os.path.join(current_path,'models'))

endpoints = fastapi.FastAPI()

@endpoints.post("/extractor")
def from_info_extractor(file:UploadFile=File(...)):

    file_savePath =  os.path.join(temp_path,file.filename)

    with open(file_savePath,'wb') as f:
        shutil.copyfileobj(file.file, f)
    
    img = cv2.imread(file_savePath)
    results = ocr_extractor.text_extract(img)

    return {
        "Message":"File is saved successfully",
        "data":file.filename,
        "results":results,
    }

@endpoints.get("/")
def ping():

    data = {
        "Message_code":200,
        "Message":"Alive"
    }

    return data


