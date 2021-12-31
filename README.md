## Computr-Vision Handwritten text extractor API

This application is based on [hugginface](https://huggingface.co/) library, in particular [microsoft/trocr-base-handwritten](https://huggingface.co/microsoft/trocr-base-handwritten). 

*API runs on the `10000` port and have the following endpoints:-*
+ ``/isAlive``  - *(get)* To verify and check the API running successfullly.
sample CURL command 
```
curl -X 'GET' \
  'http://0.0.0.0:10000/isAlive' \
  -H 'accept: application/json'
```
sample output,
```
{
  "Message_code": 200,
  "Message": "Alive"
}
```


+ ``/extractor`` - *(post)* Upload the image to to extract the Image written text in and return.
sample CURL command,
```
curl -X 'POST' \
  'http://0.0.0.0:10000/extractor' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@sample.jpg;type=image/jpeg'
```

sample output 
```
{
  "Message": "File is saved successfully",
  "data": "sample.jpg",
  "results": "Robert Crane"
}
```


Application is based on following python library stack- 
+ [fastapi](https://fastapi.tiangolo.com/)
+ [huggingface](https://huggingface.co/)
+ [OpenCV](https://opencv.org/)

#### To deploy the service -

Using docker,
```
docker build -t ocrExtractorImg .
```
And run the docker 
```
docker run -p 10000:10000 --name ocrContinaer ocrExtractorImg
```
*Optionally pre-build huggingface models could by volumn mounted*
```
docker run -p 10000:10000 --name ocrContinaer -v <local_path>/models:/models ocrExtractorImg
```

To use in the local environment, following these steps:
+ Install ``requirements.txt``
```
pip install -r requirements.txt
```

+ Run the server, *This will automatically create the two folder models and temp to which will automatically download the models from the hugginface. 
```
python src/server.py
```

