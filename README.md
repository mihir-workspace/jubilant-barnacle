## Computr-Vision Handwritten text extractor API

This application is based on [hugginface](https://huggingface.co/) library, in particular [microsoft/trocr-base-handwritten](https://huggingface.co/microsoft/trocr-base-handwritten). 

API runs on the 10000 port and have the following endpoints that it has,
+ ``/isAlive``  - *(get)* To verify and check the API running successfullly.

+ ``extractor`` - *(post)* Upload the image to to extract the Image written text in and return.

Application is based on following python library stack- 
+ [fastapi](https://fastapi.tiangolo.com/)
+ [huggingface](https://huggingface.co/)
+ [OpenCV](https://opencv.org/)~

To use in the local environment, following these steps:
+ Install ``requirements.txt``
```
pip install -r requirements.txt
```

+ Run the server, *This will automatically create the two folder models and temp to which will automatically download the models from the hugginface. 
```
python src/server.py
```

