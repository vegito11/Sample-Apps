from flask import Flask, jsonify, abort
import os
from controllers.player_controller import player_controller
from controllers.test_controller import test_controller
from controllers.aws_controller import aws_controller

app = Flask(__name__)

app.register_blueprint(player_controller)
app.register_blueprint(test_controller)
app.register_blueprint(aws_controller)

# Counter to keep track of the number of health check calls
health_check_counter = 0

# Define a threshold for failure (e.g., fail after 4 calls)
FAILURE_THRESHOLD = os.getenv("FAILURE_THRESHOLD", 4)

# Define a route for the health check
@app.route('/health_check', methods=['GET'])
def health_check():
    global health_check_counter
    health_check_counter += 1
    
    if health_check_counter <= FAILURE_THRESHOLD:
        return jsonify(status="Healthy")
    else:
        # Simulate a failing health check by returning an error status code (e.g., 500)
        abort(500)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
