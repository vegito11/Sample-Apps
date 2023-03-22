FROM python:3.9-slim-buster

ENV PYTHONPATH /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN export 

COPY . .

CMD ["python", "app.py"]
