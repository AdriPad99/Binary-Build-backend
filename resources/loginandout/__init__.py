from flask_smorest import Blueprint

bpusr = Blueprint('user', 'user', description='Contains all the information of the users.')

from . import loginandout