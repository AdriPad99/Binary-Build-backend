from flask_smorest import Blueprint

bpworkout = Blueprint('workout', 'workout', description='contains all the information of the workouts.')

from . import workouts