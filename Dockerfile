FROM python:3.9-slim-buster

ENV PYTHONPATH /app

WORKDIR /app

RUN apt update && apt install curl -y

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
