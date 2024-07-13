import os

class Config:
    # MongoDB Configuration
    MONGO_URL = os.getenv('MONGO_URL')
    MONGO_USERNAME = os.getenv('MONGO_USERNAME')
    MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
