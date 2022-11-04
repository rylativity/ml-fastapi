from fastapi import FastAPI
from fastapi.logger import logger
from model import run_inference
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


@app.get("/ml/infer")
async def infer(value: float):

    return run_inference(value)

