from models.workout_model import workoutModel

from flask import jsonify

from flask.views import MethodView

from flask_smorest import abort

from flask_jwt_extended import jwt_required

from schemas import workoutsSchema

from . import bpworkout

@bpworkout.route('/workouts')
class workoutResourceList(MethodView):
    #requires the user to be logged in
    #@jwt_required()
    @bpworkout.response(200, workoutsSchema(many=True))
    def get(self):
        try:
            #grab the contents of the table
           return workoutModel.query.all()
        except:
            abort(400, message='A problem occurred geting info from the db.')

    #@jwt_required()
    @bpworkout.arguments(workoutsSchema)
    @bpworkout.response(201, workoutsSchema)
    def post(self, data):
        try:
            workout_layout = workoutModel()

            workout_layout.from_workout(data)

            workout_layout.save_workout()

            return {'Confirmed' : 'Workout was successfully added to the products database.'}

        except:

            abort(400, message = 'There was a problem entering it into the database.')

@bpworkout.route('/workouts/<int:id>')
class workoutResource(MethodView):

    #@jwt_required()
    @bpworkout.arguments(workoutsSchema)
    def put(self, data, id):

        workout = workoutModel.query.get(id)

        try:

            workout.from_workout(data)

            workout.save_workout()
            return {"Confirmed" : "Provided workout has updated successfully."}
        except:
            abort(400, message = 'There is no workout with that id.')


    #@jwt_required()
    def delete(self, id):

        workout = workoutModel.query.get(id)

        if workout:

            workout.del_workout()
            return {'Confirmation' : 'Workout is now deleted from the product selections.'}
        else:

            abort(400, message = 'Workout with that ID not found.')