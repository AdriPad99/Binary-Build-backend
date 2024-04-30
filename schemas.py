from marshmallow import Schema, fields

#Schema for the workouts
class workoutsSchema(Schema):
    muscle_group = fields.Str(required=True)
    equipment = fields.Str(required=True)
    rep_range = fields.Int(required = True)
    weight_range = fields.Int(required=True)
    workout_variation = fields.Str(required=True)

#Schema for the user
class userSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)