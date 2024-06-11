from flask import Flask, jsonify, abort
import os
from loggers.logger import logger
from controllers.log_generator import loggen_controller

app = Flask(__name__)
app.register_blueprint(loggen_controller)

@app.route('/health_check', methods=['GET'])
def health_check():
    logger.info("showing healthcheck")
    return jsonify(status=f"Healthy - OK")

@app.route('/')
def home():
    app_logger.info('Home route accessed')
    return 'Welcome to the Flask Logging App!'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')