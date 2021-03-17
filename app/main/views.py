from flask.globals import request
import datetime
import base64
from app.main.forms import UpdateDocterAccount, UpdatePatientAccount, ExampleForm
from werkzeug.utils import redirect
from app import main
from flask import render_template, redirect, url_for, g, session, flash
from . import main
from .. import db
from ..model import Appointment, Doctor, Patient
@main.before_request
def before_request():
    if 'email' in session and 'user' in session:
        if session['user'] == 'val2':
            user = Patient.query.filter_by(email=session['email']).first()
            g.user = user
        else:
            user = Doctor.query.filter_by(email=session['email']).first()
            g.user = user
    else:
        g.user = None

@main.route("/")
def index():
    if not g.user:
        return redirect(url_for('auth.login'))
    return render_template('index.html')

@main.route("/docters")
def docters():
    dokters = Doctor.query.all()
    docs =[]
    for dokter in dokters:
        dokter.image = base64.b64encode(dokter.image).decode('ascii')
    return render_template("mainapp/docters.html", dokters=dokters)

@main.route("/account", methods=["GET", "POST"])
def account():
    if "email" in session:
        image_file = None
        user = session["user"]
        form = UpdatePatientAccount() if user == "val2" else UpdateDocterAccount()
        if request.method == "GET":
            if user == "val2":
                pasien = Patient.query.filter_by(email=session["email"]).first()
                form.username.data = pasien.name
                form.email.data = pasien.email
                form.gender.data = pasien.gender
                form.age.data = pasien.age
                form.address.data = pasien.address
                if not pasien.image:
                    image_file = url_for("static", filename="karlo.jpg")
                else:
                    image_file = base64.b64encode(pasien.image).decode('ascii')
            elif user == "val1":
                dokter = Doctor.query.filter_by(email=session["email"]).first()
                form.username.data = dokter.name
                form.email.data = dokter.email
                form.speciality.data = dokter.speciality
                form.address.data = dokter.address
                if not dokter.image:
                    image_file = url_for("static", filename="karlo.jpg")
                else:
                    image_file = base64.b64encode(dokter.image).decode('ascii')
            else:
                pass
        elif form.validate_on_submit():
            if user == "val2":
                pasien = Patient.query.filter_by(email=session["email"]).first()
                pasien.name = form.username.data
                pasien.email = form.email.data
                pasien.gender = form.gender.data
                pasien.age = form.age.data
                pasien.address = form.address.data
                pasien.image = form.file_img.data.read()
                db.session.commit()
                flash("Data has been updated", "success")
                return redirect(url_for("main.account"))
            elif user == "val1":
                dokter = Doctor.query.filter_by(email=session["email"]).first()
                dokter.name = form.username.data
                dokter.email = form.email.data
                dokter.speciality = form.speciality.data
                dokter.address =form.address.data
                dokter.image = form.file_img.data.read()
                db.session.commit()
                flash("Data dokter sudah diupdata", "success")
                return redirect(url_for("main.account"))
            else:
                pass
        return render_template('mainapp/account.html', form=form, image_file=image_file)

@main.route("/appointment", methods=["POST", "GET"])
def appointment():
    if "email" in session:
        form = ExampleForm()
        form.dokters.choices = [ (str(dokter.id_doc), dokter.name) for dokter in Doctor.query.all()]
        if session["user"] == "val2":
            pasien = Patient.query.filter_by(email=session["email"]).first()
            if form.validate_on_submit():
                date = datetime.datetime.fromordinal(form.dt.data.toordinal())
                dokter = Doctor.query.filter_by(id_doc=int(form.dokters.data)).first()
                janji = Appointment(diagnosis='', treatment='', tanggal=date)
                dokter.app_docs.append(janji)
                pasien.app_pats.append(janji)
                db.session.add(janji)
                db.session.commit()
                flash(f"Appointment has been added!{dokter.name} {pasien.name} {date}")
            return render_template("mainapp/appointment.html", form=form)
        elif session["user"] == "val1":
            dokter = Doctor.query.filter_by(email=session["email"]).first()
            appointments = Appointment.query.filter_by(id_docter=dokter.id_doc).all()
            if appointments:
                return render_template("mainapp/docappointment.html", values=appointments)

    else:
        return redirect(url_for("auth.login"))

@main.route("/updatedata", methods=["GET", "POST"])
def updatedata():
    if request.method == "POST":
        appointment = Appointment.query.filter_by(id_app=request.form.get("id")).first()
        if appointment:
            appointment.diagnosis = request.form["diagnosa"]
            appointment.treatment = request.form["treat"]

            db.session.commit()
            flash(f"Data has been update!{request.form.get('id')}")
            return redirect(url_for("main.appointment"))

        





