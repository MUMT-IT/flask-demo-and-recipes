from flask import render_template, flash, redirect, url_for, jsonify

from app.user.forms import RegisterForm
from app.user.models import User
from app.main import db
from . import user_blueprint as user


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


@user.route('/appointments')
def make_appointment():
    return 'You can make an appointment now.'


@user.route('/api/v1.0/services')
def get_services():
    services = ['Check up', 'Counseling', 'Special tests', 'Health & Wellness']
    return jsonify({'data': services})

