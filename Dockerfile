FROM python:3.9-slim
WORKDIR /usr/src/app

COPY req.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r req.txt

COPY . .

EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
