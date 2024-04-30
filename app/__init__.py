import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_PROJ_URL')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_model import userModel
from models.workout_model import workoutModel