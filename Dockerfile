FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN touch secrets.env
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]