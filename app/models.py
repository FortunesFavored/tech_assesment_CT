from app import db
from datetime import datetime

class divvyData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, nullable=False, unique=False)
    start_time = db.Column(db.DateTime(), nullable=False, unique=False)
    stop_time = db.Column(db.DateTime(), nullable=False, unique=False)
    bike_id = db.Column(db.Integer, nullable=False, unique=False)
    from_station_id = db.Column(db.Integer, nullable=False, unique=False)
    from_station_name = db.Column(db.String(250), nullable=False, unique=False)
    to_station_id = db.Column(db.Integer, nullable=False, unique=False)
    to_station_name = db.Column(db.String(250), nullable=False, unique=False)
    user_type = db.Column(db.String(150), nullable=False, unique=False)
    gender = db.Column(db.String(150), nullable=True, unique=False)
    birthday = db.Column(db.String(150), nullable=True, unique=False)
    trip_duration = db.Column(db.Integer, nullable=False, unique=False)

    def __init__(self, trip_id, start_time, stop_time, bike_id, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthday,trip_duration):
        self.trip_id = trip_id
        self.start_time = start_time
        self.stop_time
        self.bike_id
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_duration


