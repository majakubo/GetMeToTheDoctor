from db import db


class Shift(db.Model):
    __tablename__ = "shift"
    id = db.Column(db.Integer, primary_key=True)
    bgn_hour = db.Column(db.DateTime())
    end_hour = db.Column(db.DateTime())
    office_id = db.Column(db.Integer, db.ForeignKey('office.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))

    def __init__(self, bgn_hour, end_hour, office_id, doctor_id):
        self.bgn_hour = bgn_hour
        self.end_hour = end_hour
        self.office_id = office_id
        self.doctor_id = doctor_id
