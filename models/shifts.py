from db import db


class Shift(db.Model):
    __tablename__ = "shift"
    id = db.Column(db.Integer, primary_key=True)
    bgn_hour = db.Column(db.DateTime())
    end_hour = db.Column(db.DateTime())
    office_id = db.Column(db.Integer, db.ForeignKey('office.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
