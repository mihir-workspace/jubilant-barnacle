import uvicorn
import os
from handwritten import model_installer
from handwritten import OCRExtractor

if __name__=='__main__':

    parent_path  = os.path.dirname(os.getcwd())

    # Check the model and it's config exits or not
    if not os.listdir(os.path.join(parent_path,'models')):

        model_installer(os.path.join(parent_path,'models'))

    # Check the temp folder exits or not for temp image saving
    temp_path = os.path.join(parent_path,'temp')
    if os.path.exists(temp_path)==False:
        os.mkdir('temp')
    

    # Launch the API server
    uvicorn.run("api:endpoints",host="0.0.0.0",port=10000,reload=True)