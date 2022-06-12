import os

from flask import Flask, render_template
from dotenv import load_dotenv
from models import *

load_dotenv()

app = Flask(__name__)  # file name
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.init_app(app)


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
