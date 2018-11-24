from db import db


class Doctor(db.Model):
    __tablename__ = "doctor"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    specialization = db.Column(db.String(80))
    shift = db.relationship('Shift', lazy='dynamic')

    def __init__(self, firstname, lastname, specialization):
        self.firstname = firstname
        self.lastname = lastname
        self.specialization = specialization
