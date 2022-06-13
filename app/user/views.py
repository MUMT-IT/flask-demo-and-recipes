from datetime import datetime

from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import login_required

from app.user.forms import RegisterForm, AppointmentForm
from app.models import User, Appointment
from app.main import db
from . import user_blueprint as user
from pytz import timezone

Bangkok = timezone('Asia/Bangkok')


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        new_user = User(
            name=name,
            email=email,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        flash('You have registered successfully.')
        return redirect(url_for('show_menu'))
    return render_template('register.html', form=form, errors=form.errors)


@user.route('/appointments', methods=['GET', 'POST'])
@login_required
def make_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        new_apt = Appointment()
        form.populate_obj(new_apt)  # insert data from form to model
        db.session.add(new_apt)
        db.session.commit()
        flash('Data has been saved.')
        return redirect(url_for('show_menu'))
    return render_template('appointment.html', form=form)


@user.route('/appointments/<int:apt_id>/confirm')
def confirm_appointment(apt_id):
    appointment = Appointment.query.get(apt_id)
    appointment.confirmed_at = datetime.now(tz=Bangkok)
    db.session.add(appointment)
    db.session.commit()
    flash('The appointment ID={} has been confirmed'.format(apt_id))
    return redirect(url_for('list_appointments'))


@user.route('/api/v1.0/services')
def get_services():
    services = ['Check up', 'Counseling', 'Special tests', 'Health & Wellness']
    return jsonify({'data': services})

