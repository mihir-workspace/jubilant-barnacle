import uvicorn
import os
if __name__=='__main__':

    current_path = os.getcwd()
    temp_path = os.path.join(current_path,'temp')
    if os.path.exists(temp_path)==False:
        os.mkdir('temp')
    
    # Launch the API server
    uvicorn.run("api:endpoints",host="0.0.0.0",port=10000,reload=True)