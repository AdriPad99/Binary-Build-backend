from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class userModel(db.Model):

    #sets table name
    __tablename__ = 'users'

    #sets outline for table
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), nullable = False, unique = True) #unique
    email = db.Column(db.String(50), nullable = False, unique = True) #unique
    password = db.Column(db.String, nullable = False, unique = False)
    first_name = db.Column(db.String(20), nullable = False, unique = False)
    last_name = db.Column(db.String(20), nullable = False, unique = False)
    summary = db.Column(db.String(400), nullable = False, unique = False)
    age = db.Column(db.Integer, nullable = True, unique = False)
    gender = db.Column(db.String(20), nullable = True, unique = False)
    height = db.Column(db.String(50), nullable = True, unique = False)
    weight = db.Column(db.Integer, nullable = True, unique = False)
    target_weight = db.Column(db.Integer, nullable = True, unique = False)
    target_body_fat_percentage = db.Column(db.Integer, nullable = True, unique = False)
    fitness_level = db.Column(db.String(15), nullable = True, unique = False)
    daily_activity_level = db.Column(db.String(15), nullable = True, unique = False)
    pref_workout_types = db.Column(db.String(20), nullable = True, unique = False)
    pref_workout_duration = db.Column(db.Integer, nullable = True, unique = False)
    available_equipment = db.Column(db.String(200), nullable = True, unique = False)
    chest = db.Column(db.Integer, nullable = True, unique = False)
    waist = db.Column(db.Integer, nullable = True, unique = False)
    hips = db.Column(db.Integer, nullable = True, unique = False)
    amnt_workouts_completed = db.Column(db.Integer, nullable = True, unique = False)

    #adds and commits local information
    def add_usr(self):
        db.session.add(self)
        db.session.commit()

    #saves local information to the database
    def save_usr(self):
        db.session.add(self)
        db.session.commit()

    #deletes information from the database
    def del_usr(self):
        db.session.delete(self)
        db.session.commit()

    #forms the requests for the database
    def from_usr(self, dict):
        for k, v in dict.items():
            if k != 'password':
                setattr(self, k, v)	##sets attribute
            else:
                setattr(self, 'password', generate_password_hash(v))

    #checks object password against password passed in as argument with the 
    #check_password_hash functionallity.
    def check_usr_password(self, password):
        return check_password_hash(self.password, password)