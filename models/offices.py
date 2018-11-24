from db import db


class Office(db.Model):
    __tablename__ = "office"
    id = db.Column(db.Integer, primary_key=True)
    qr = db.Column(db.String)
    shift = db.relationship('Shift', lazy='dynamic')
