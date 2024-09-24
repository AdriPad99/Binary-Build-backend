from marshmallow import Schema, fields

#Schema for the workouts
class workoutsSchema(Schema):
    workout_id = fields.Int(dump_only = True)
    muscle_group = fields.Str(required=True)
    equipment = fields.Str(required=True)
    rep_range = fields.Int(required = True)
    weight_range = fields.Int(required=True)
    workout_variation = fields.Str(required=True)
    day = fields.Str(required=True)

#Schema for the random workouts
class randomWorkoutsSchema(Schema):
    workout_id = fields.Int(dump_only = True)
    muscle_group = fields.Str(required=True)
    equipment = fields.Str(required=True)
    rep_range = fields.Int(required = True)
    weight_range = fields.Int(required=True)
    workout_variation = fields.Str(required=True)
    day = fields.Str(required=True)

#Schema for the user
class userSchema(Schema):
    user_id = fields.Int(dump_only=True)
    username = fields.Str(required=False)
    email = fields.Str(required=False)
    password = fields.Str(required=False)
    first_name = fields.Str(required=False)
    last_name = fields.Str(required=False)
    summary = fields.Str(required=False)
    age = fields.Int(required = False)
    gender = fields.Str(required = False)
    height = fields.Str(required=False)
    weight = fields.Str(required=False)
    target_weight = fields.Int(required=False)
    target_body_fat_percentage = fields.Int(required=False)
    fitness_level = fields.Str(required=False)
    daily_activity_level = fields.Str(required=False)
    pref_workout_types = fields.Str(required=False)
    pref_workout_duration = fields.Int(required=False)
    available_equipment = fields.Str(required=False)
    chest = fields.Int(required=False)
    waist = fields.Int(required=False)
    hips = fields.Int(required=False)
    amnt_workouts_completed = fields.Int(required=False)
    # calories = fields.Int(required=False)
    # weight_loss = fields.Int(required=False)
    # max_weight_lifted = fields.Int(required=False)
    # fastest_mile = fields.Int(required=False)
    # total_workout_time = fields.Int(required=False)
    # total_calories_burned = fields.Int(required=False)
    # total_workouts_completed = fields.Int(required=False)
    # total_workout_time = fields.Int(required=False)