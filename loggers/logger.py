import logging
import json
import os
import sys
from logging.handlers import RotatingFileHandler

# Read environment variables to configure logging
app_name = os.getenv('APP_NAME', 'app1')  # Enable or disable console logging
cli_log = os.getenv('CONSOLE_LOG', 'enabled')  # Enable or disable console logging
file_log = os.getenv('FILE_LOG', 'enabled')    # Enable or disable file logging
log_type = os.getenv('LOG_TYPE', 'json')       # Set log format type (json or text)
app_log_path = os.getenv('APP_LOG_PATH', 'logs/app.log')  # Path for the application log file
access_log_path = os.getenv('ACCESS_LOG_PATH', 'logs/access.log')  # Path for the access log file

# Ensure the log directories exist
os.makedirs(os.path.dirname(app_log_path), exist_ok=True)

# Custom JSON formatter for logs
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'appname': app_name,
            'module': record.module,
            'line_no': record.lineno,
            'function': record.funcName
        }
        return json.dumps(log_record)

# Define the log format for text logs
formatter = f'[{app_name}] [%(levelname)s] [%(asctime)s] %(lineno)d - %(message)s'
log_format = logging.Formatter(formatter)

# Configure the application logger
app_logger = logging.getLogger('rand_logger')
app_logger.setLevel(logging.DEBUG) 

## Update the default flask logger setting
werkzeug_logger = logging.getLogger('werkzeug')

# Configure file logging if enabled
if file_log == "enabled":
	
	file_handler = RotatingFileHandler(app_log_path, maxBytes=10000, backupCount=1)

	if log_type == "json":
		json_formatter = JsonFormatter()
		file_handler.setFormatter(json_formatter)
	else:
		file_handler.setFormatter(log_format)
	
	app_logger.addHandler(file_handler)
	
	werkzeug_filehandler = RotatingFileHandler(access_log_path, maxBytes=10000, backupCount=1)
	werkzeug_filehandler.setFormatter(log_format)
	werkzeug_logger.addHandler(werkzeug_filehandler)

# Configure console logging if enabled
if cli_log == "enabled":
	console = logging.StreamHandler(sys.stdout)
	console.setFormatter(log_format)
	
	app_logger.addHandler(console)
	werkzeug_logger.addHandler(console)

# logging.getLogger('werkzeug').disabled = True