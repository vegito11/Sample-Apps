from flask import Flask
from controllers.player_controller import player_controller
from controllers.test_controller import test_controller

app = Flask(__name__)

app.register_blueprint(player_controller)
app.register_blueprint(test_controller)

if __name__ == '__main__':
    app.run()
