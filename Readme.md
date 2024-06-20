# Flask Logging App

   - This Flask application is a simple logging system that generates and logs various types of messages. 

   - It provides routes to generate random logs, debug logs, error logs, and exception logs.

   - This project provides a Python logging configuration that 

      1. can log messages to both the `console` and a `file`.
      
      2. The **log format** can be in plain `text` or `JSON` format based on environment variables. 

      The configuration includes handling for rotating file logs and integrates with Flask's `werkzeug` logger.

   
     ### Features

       1. Logs messages to the `console` and/or `file`.

       1. Supports both plain `text` and `JSON` log formats.
    
       1. Uses rotating file handlers to manage log file sizes.
    
       1. Environment variables for easy configuration.

       1. Generate random logs of different levels: `debug`, `info`, `warning`, `error`, `critical`.

----------------------

## Environment Variables

   The following environment variables can be set to configure the logging behavior:

   - `APP_NAME`: Name of the application (default: `app1`).
   
   - `CONSOLE_LOG`: Enable or disable logging to the console (`enabled` or `disabled`, default: `enabled`).
   
   - `FILE_LOG`: Enable or disable logging to a file (`enabled` or `disabled`, default: `enabled`).
   
   - `LOG_TYPE`: Type of log format (`json` or `text`, default: `json`).
   
   - `APP_LOG_PATH`: Path to the application log file (default: `logs/app.log`).
   
   - `ACCESS_LOG_PATH`: Path to the access log file (default: `logs/access.log`).

        ```bash
        export APP_NAME=myapp
        export CONSOLE_LOG=enabled
        export FILE_LOG=enabled
        export LOG_TYPE=json
        export APP_LOG_PATH=logs/myapp.log
        export ACCESS_LOG_PATH=logs/access.log
        ```

        In this example, logs will be written to both the console and `logs/myapp.log` in JSON format, and the access logs will be written to `logs/access.log`.

      > Note: Adjust the file sizes and backup counts in `RotatingFileHandler` as needed for your use case.   

--------------------------------------

## Project Structure

   - **`app.py`**: The main script to run the Flask application and define routes.

   - **`controllers/log_generator.py`**: Blueprint defining routes for generating logs.
       
       Log generation logic is defined in `controllers/log_generator.py`. 
       
       It provides routes to generate random logs, debug logs, error logs, and exception logs.

   - **`loggers/logger.py`**: 

        The logging configuration is set up in `loggers/logger.py`. It supports logging to `console` and `file` based on environment variables.

   - **`requirements.txt`**: File containing the dependencies required to run the application.

     ```bash
     ├── app.py
     ├── controllers
     │   └── log_generator.py
     ├── loggers
     │   └── logger.py
     ├── logs
     │   └── app.log
     └── requirements.txt
     ```

--------------------

## Usage

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
    - Generate mixed Log: `http://localhost:5000/generate-mixed`

-----------------------------------------

## Endpoints

1. **`/generate-exception`**
   
   - Simulates exceptions to test error handling.
   
   - Generates 1 to 3 exceptions with a delay between them.
   
   - **Response**: A message indicating exceptions were generated.

2. **`/generate-mixed`**
   
   - Generates a mix of log messages with varying log levels.
   
   - Log levels include: `debug`, `info`, `warning`, `error`, `critical`.
   
   - Generates between 2 to 8 log messages with a delay between them.
   
   - **Response**: A message indicating mixed logs were generated.

-----------------------------------------

## Reference

- [Log Format Variables](https://docs.python.org/3/library/logging.html#logrecord-attributes)