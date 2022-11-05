from model import classify_image

from fastapi import FastAPI, File, UploadFile
from fastapi.logger import logger

from io import BytesIO
import logging

### https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/issues/19
gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers
if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)
# DEBUG > INFO > WARN > ERROR > CRITICAL > FATAL

app = FastAPI(debug=True)

@app.get("/")
async def root():
    logger.warn("LOGGING WORKS!!")

    return {"message":"Goodbye"}


@app.post("/classify_image")
async def run_classify_image(image_file: UploadFile = File(...)):

    img = BytesIO(image_file.file.read())

    resp = classify_image(img)
    logger.warn(type(resp))
    logger.warn(resp)
    
    return resp

