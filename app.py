from flask import Flask
from dotenv import load_dotenv
import os
from routes.player_routes import player_bp
from routes.memory_routes import memory_bp

load_dotenv()

app = Flask(__name__)

# Load MongoDB connection details from environment variables
app.config['MONGO_URL'] = os.getenv('MONGO_URL')
app.config['MONGO_USERNAME'] = os.getenv('MONGO_USERNAME')
app.config['MONGO_PASSWORD'] = os.getenv('MONGO_PASSWORD')

app.register_blueprint(player_bp, url_prefix='/api')
app.register_blueprint(memory_bp, url_prefix='/memory')

if __name__ == '__main__':
    app.run(debug=True)
