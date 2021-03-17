from flask import render_template, url_for, redirect, flash, session, g
from . import auth
from .forms import LoginForm, RegistrationForm 
from ..model import Patient, Doctor
from .. import db

@auth.before_request
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



@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.example.data
        if user:
            session['user'] = user
            if user == 'val2':
                found_user = Patient.query.filter_by(email=form.email.data).first()
                if found_user is not None and found_user.password == form.password.data:
                    session['email'] = form.email.data
                    return redirect(url_for('main.index'))
                else:
                    flash("Bad email or password!")
                    return redirect(url_for('auth.login'))
            else:
                found_user = Doctor.query.filter_by(email=form.email.data).first()
                if found_user is not None and found_user.password == form.password.data:
                    session['email'] = form.email.data
                    return redirect(url_for('main.index'))
                else:
                    flash("Bad email or password!")
                    return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_type = form.example.data
        if user_type == 'val2':
            pasien = Patient(name=form.username.data, email=form.email.data, gender='', age='',
                             password=form.password.data, address='')
            db.session.add(pasien)
            db.session.commit()
            flash("Pasien sudah ditambahkan.")
            return redirect(url_for('auth.login'))
        if user_type == 'val1':
            docter = Doctor(name=form.username.data, speciality='', password=form.password.data,
                            email=form.email.data)
            db.session.add(docter)
            db.session.commit()
            flash("Dokter sudah ditambahkan")
            return redirect(url_for('auth.login'))
    return render_template('auth/registration.html', form=form)

@auth.route('/logout')
def logout():
    if 'email' in session:
        flash("you've been logout")
        session.pop('user', None)
        session.pop('email', None)
    return redirect(url_for('auth.login'))
