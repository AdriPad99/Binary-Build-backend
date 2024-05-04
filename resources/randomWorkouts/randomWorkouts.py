from models.random_workout_model import randomWorkoutModel

from flask import jsonify

from flask.views import MethodView

from flask_smorest import abort

from flask_jwt_extended import jwt_required

from schemas import randomWorkoutsSchema

from . import bpranworkout

@bpranworkout.route('/randomWorkouts')
class workoutResourceList(MethodView):
    #requires the user to be logged in
    #@jwt_required()
    @bpranworkout.response(200, randomWorkoutsSchema(many=True))
    def get(self):
        try:
            #grab the contents of the table
           return randomWorkoutModel.query.all()
        except:
            abort(400, message='A problem occurred geting info from the db.')

    #@jwt_required()
    @bpranworkout.arguments(randomWorkoutsSchema)
    @bpranworkout.response(201, randomWorkoutsSchema)
    def post(self, data):
        try:
            random_workout_layout = randomWorkoutModel()

            random_workout_layout.from_random_workout(data)

            random_workout_layout.save_random_workout()

            return {'Confirmed' : 'Workout was successfully added to the products database.'}

        except:

            abort(400, message = 'There was a problem entering it into the database.')

@bpranworkout.route('/randomWorkouts/<int:id>')
class workoutResource(MethodView):

    #@jwt_required()
    @bpranworkout.arguments(randomWorkoutsSchema)
    def put(self, data, id):

        random_workout_layout = randomWorkoutModel.query.get(id)

        try:

            random_workout_layout.from_random_workout(data)

            random_workout_layout.save_random_workout()
            return {"Confirmed" : "Provided workout has updated successfully."}
        except:
            abort(400, message = 'There is no workout with that id.')


    def get(self,id):
        random_workout_layout = randomWorkoutModel.query.get(id)

        if random_workout_layout:
            return {"Workout ID" : random_workout_layout.workout_id,
                    "Equipment" : random_workout_layout.equipment,
                    "Muscle Group" : random_workout_layout.muscle_group,
                    "Rep Range" : random_workout_layout.rep_range,
                    "Weight Range" : random_workout_layout.weight_range,
                    "Workout Variation" : random_workout_layout.workout_variation}, 200
        else:
            return {"error" : "No random workout with that information inthe database."}, 400


    #@jwt_required()
    def delete(self, id):

        random_workout_layout = randomWorkoutModel.query.get(id)

        if random_workout_layout:

            random_workout_layout.del_random_workout()
            return {'Confirmation' : 'Workout is now deleted from the product selections.'}
        else:

            abort(400, message = 'Workout with that ID not found.')