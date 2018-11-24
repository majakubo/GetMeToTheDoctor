from db import db


class Doctor(db.Model):
    __tablename__ = "doctor"
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(80))
    specialization = db.Column(db.String(80))
    shift = db.relationship('Shift', lazy='dynamic')
