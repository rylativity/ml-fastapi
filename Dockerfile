FROM python:3.10

WORKDIR /workspace

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY *.py ./

CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--log-level", "debug", "--reload"]