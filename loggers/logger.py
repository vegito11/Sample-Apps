import logging
import os
import sys

# Ensure the log directories exist
cli_log = os.getenv('CONSOLE_LOG', 'enabled')
file_log = os.getenv('FILE_LOG', 'enabled')
app_log_path = os.getenv('APP_LOG_PATH', 'logs/app.log')
os.makedirs(os.path.dirname(app_log_path), exist_ok=True)
formatter = '[%(levelname)s] [%(asctime)s] %(lineno)d - %(message)s'
handlers = []

if file_log == "enabled":
	file_handler = logging.FileHandler(app_log_path)
	log_format = logging.Formatter(formatter)
	file_handler.setFormatter(log_format)
	handlers.append(file_handler)

if cli_log == "enabled":
	console = logging.StreamHandler(sys.stdout)
	handlers.append(console)

logger = logging.getLogger('rand_logger')
logging.basicConfig(level=logging.DEBUG, format=formatter, handlers=handlers)