import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_PROJ_URL')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_model import userModel
from models.workout_model import workoutModel
from models.random_workout_model import randomWorkoutModel

from resources.loginandout import bpusr as login_bp
app.register_blueprint(login_bp)
from resources.workouts import bpworkout as workout_bp
app.register_blueprint(workout_bp)
from resources.randomWorkouts import bpranworkout as ranWorkout_bp
app.register_blueprint(ranWorkout_bp)