from flask import Blueprint, jsonify, request
import random
import string
import time

from loggers.logger import app_logger
from utils.utility import (log_templates, users, 
actions, items, random_exception_generator)

loggen_controller = Blueprint('loggen_controller', __name__)

def generate_random_log_message(log_level):
    template = random.choice(log_templates[log_level])
    user = random.choice(users)
    action = random.choice(actions)
    item = random.choice(items)
    return template.format(user, item)

@loggen_controller.route('/random-log')
def random_log():
    log_level = random.choice(['debug', 'info', 'warning', 'error', 'critical'])
    message = generate_random_log_message(log_level)
    
    if log_level == 'debug':
        app_logger.debug(message)
    elif log_level == 'info':
        app_logger.info(message)
    elif log_level == 'warning':
        app_logger.warning(message)
    elif log_level == 'error':
        app_logger.error(message)
    elif log_level == 'critical':
        app_logger.critical(message)

    return f'Generated a {log_level} log.'

@loggen_controller.route('/generate-debug')
def generate_debug():
    message = generate_random_log_message('debug')
    app_logger.debug(message)
    return 'Generated a debug log.'

@loggen_controller.route('/generate-error')
def generate_error():
    message = generate_random_log_message('error')
    app_logger.error(message)
    return 'Generated an error log.'

@loggen_controller.route('/generate-exception')
def generate_exception():
    for _ in range(random.randint(1, 3)):
        random_exception_generator()
        time.sleep(0.7)

    return 'Generated an exception log.'

@loggen_controller.route('/generate-mixed')
def generate_mixed():
    log_levels = ['debug', 'info', 'warning', 'error', 'critical']
    
    for _ in range(random.randint(2, 8)):
        log_level = random.choice(log_levels)
        message = generate_random_log_message(log_level)
        time.sleep(0.7)
        
        if log_level == 'debug':
            app_logger.debug(message)
        elif log_level == 'info':
            app_logger.info(message)
        elif log_level == 'warning':
            app_logger.warning(message)
        elif log_level == 'error':
            app_logger.error(message)
        elif log_level == 'critical':
            app_logger.critical(message)

    return 'Generated mixed logs.'
