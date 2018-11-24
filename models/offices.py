from db import db
1
class Office(db.Model):
    __tablename__ = "office"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    qr_code = db.Column(db.String)
    shift = db.relationship('Shift', lazy='dynamic')

    def __init__(self, name, qr_code):
        self.name = name
        self.qr_code = qr_code

