import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)  # file name
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

from app.user.models import *

db.create_all()


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
