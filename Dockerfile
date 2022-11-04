FROM python:3

WORKDIR /workspace

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY tf_model_weights ./tf_model_weights/

COPY *.py ./

CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--log-level", "debug", "--reload"]