import os

from flask import Flask, render_template, flash, redirect, url_for, request
from flask_migrate import Migrate
from dotenv import load_dotenv
from sqlalchemy.orm.exc import NoResultFound

from models import *
from app.user.forms import LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required

load_dotenv()

app = Flask(__name__)  # file name
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            user = User.query.filter_by(email=email, password=password).one()
        except NoResultFound:
            flash('Logged in unsuccessful')
        else:
            login_user(user)
            flash('Logged in successfully')
            # next = request.args.get("next")
            # if next:
            #     return redirect(next)
            # else:
            #     return redirect(url_for('index'))
            next = request.args.get("next") or url_for('index')
            return redirect(next)
    return render_template('auth/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/menus')
def show_menu():
    return render_template('menus.html')


@app.route('/appointments')
def list_appointments():
    appointments = Appointment.query.all()
    return render_template('appointment_list.html', appointments=appointments)


from user import user_blueprint
app.register_blueprint(user_blueprint)
