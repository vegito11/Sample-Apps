### Flask Logging App

This Flask application is a simple logging system that generates and logs various types of messages. It provides routes to generate random logs, debug logs, error logs, and exception logs.

### Project Structure

```
.
├── app.py
├── controllers
│   └── log_generator.py
├── Dockerfile
├── loggers
│   └── logger.py
├── logs
│   └── app.log
└── requirements.txt
```

### Components

- **`app.py`**: The main script to run the Flask application and define routes.
- **`controllers/log_generator.py`**: Blueprint defining routes for generating logs.
- **`Dockerfile`**: Dockerfile for building the application into a Docker image.
- **`loggers/logger.py`**: Logger setup script defining logging configurations.
- **`logs/app.log`**: Log file to store application logs.
- **`requirements.txt`**: File containing the dependencies required to run the application.

### Usage

1. **Setup Environment**:
    - Make sure you have Docker installed on your system.

2. **Build Docker Image**:
    ```bash
    docker build -t flask-logging-app .
    ```

3. **Run Docker Container**:
    ```bash
    docker run -p 5000:5000 flask-logging-app
    ```

4. **Access Routes**:
    - Home: `http://localhost:5000/`
    - Generate Random Log: `http://localhost:5000/random-log`
    - Generate Debug Log: `http://localhost:5000/generate-debug`
    - Generate Error Log: `http://localhost:5000/generate-error`
    - Generate Exception Log: `http://localhost:5000/generate-exception`

### Logging Configuration

The logging configuration is set up in `loggers/logger.py`. It supports logging to console and file based on environment variables.

### Log Generation

Log generation logic is defined in `controllers/log_generator.py`. It provides routes to generate random logs, debug logs, error logs, and exception logs.
