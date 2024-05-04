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


    #route that gets the information on a specific product based on id
    # @bpproduct.route('/products/<int:id>')
    # class prodResource(MethodView):
    #     def get(self, id):
    #         #grabs the product at the with the given id
    #         product = productModel.query.get(id)
    #         #if that product exists
    #         if product:
    #             #return all of its details
    #             return {"name" : product.product_name,
    #                     "price" : product.product_price,
    #                     "description" : product.product_description}, 200
    #         else:
    #             #return error if it doesn't
    #             return {"error" : "No product with that ID in the database."}, 400

    # def get(self,id):
    #     workout = workoutModel.query.get(id)

    #     if workout:
    #         return {"Workout ID" : workout.workout_id,
    #                 "Equipment" : workout.equipment,
    #                 }


    #@jwt_required()
    def delete(self, id):

        workout = workoutModel.query.get(id)

        if workout:

            workout.del_workout()
            return {'Confirmation' : 'Workout is now deleted from the product selections.'}
        else:

            abort(400, message = 'Workout with that ID not found.')