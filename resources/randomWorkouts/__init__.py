from flask_smorest import Blueprint

bpranworkout = Blueprint('randomWorkout', 'randomWorkout', description='Contains all the information of the random workouts')

from . import randomWorkouts