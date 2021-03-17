from flask_sqlalchemy import SQLAlchemy
from app import db


class Patient(db.Model):
    id_patient = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, index=True)
    email = db.Column(db.String(60), unique=True, index=True)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    password = db.Column(db.String(6))
    address = db.Column(db.String(20))
    image = db.Column(db.BLOB)
    app_pats = db.relationship('Appointment', backref='patient')

    def __repr__(self):
        return "<Patient> %r, age: %r, address: %r" % (self.name, self.age, self.address)

class Appointment(db.Model):
    id_app = db.Column(db.Integer, primary_key=True)
    id_patient = db.Column(db.Integer, db.ForeignKey('patient.id_patient'))
    id_docter = db.Column(db.Integer, db.ForeignKey('doctor.id_doc'))
    diagnosis = db.Column(db.String(50))
    treatment = db.Column(db.String(50))
    tanggal = db.Column(db.DateTime)




class Doctor(db.Model):
    id_doc = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, index=True)
    speciality = db.Column(db.String(20))
    password = db.Column(db.String(6))
    email = db.Column(db.String(60), unique=True, index=True)
    address = db.Column(db.String(20))
    image = db.Column(db.BLOB)
    app_docs = db.relationship('Appointment', backref='doctor')

    def __repr__(self):
        return "<Doctor> name: %r, spciality: %r" % (self.name, self.speciality)


