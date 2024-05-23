import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db import init_db
from config import config

app = Flask(__name__)

# Set the configuration based on the environment
env = os.environ.get('FLASK_ENV', 'default')
app.config.from_object(config[env])

# Initialize extensions
CORS(app)
jwt = JWTManager(app)

# Initialize the database
init_db()


if __name__ == '__main__':
    app.run(debug=True)