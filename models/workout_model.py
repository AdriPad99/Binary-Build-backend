from app import db

class workoutModel(db.Model):

    #sets the table name
    __tablename__ = 'workouts'

    muscle_group = db.Column(db.String, primary_key=True)
    equipment = db.Column(db.Boolean, nullable=False)
    rep_range = db.Column(db.Integer, nullable=False)
    weight_range = db.Column(db.Integer, nullable=False)
    workout_variation = db.Column(db.String, nullable=False)

    #adds and commits local information
    def add_workout(self):
        db.session.add(self)
        db.session.commit()

    #saves local information to the database
    def save_workout(self):
        db.session.add(self)
        db.session.commit()

    #deletes information from the database
    def del_workout(self):
        db.session.delete(self)
        db.session.commit()

    #forms the requests for the database
    def from_workout(self, dict):
        for k , v in dict.items():
            setattr(self, k, v)