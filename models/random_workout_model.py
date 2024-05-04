from app import db

class randomWorkoutModel(db.Model):

    #sets the table name
    __tablename__ = 'random_workouts'

    workout_id = db.Column(db.Integer, primary_key=True)
    muscle_group = db.Column(db.String, nullable=False)
    equipment = db.Column(db.String, nullable=False)
    rep_range = db.Column(db.Integer, nullable=False)
    weight_range = db.Column(db.Integer, nullable=False)
    workout_variation = db.Column(db.String, nullable=False)

    #adds and commits local information
    def add_random_workout(self):
        db.session.add(self)
        db.session.commit()

    #saves local information to the database
    def save_random_workout(self):
        db.session.add(self)
        db.session.commit()

    #deletes information from the database
    def del_random_workout(self):
        db.session.delete(self)
        db.session.commit()

    #forms the requests for the database
    def from_random_workout(self, dict):
        for k , v in dict.items():
            setattr(self, k, v)