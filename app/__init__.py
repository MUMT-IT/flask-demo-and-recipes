from flask import Flask, render_template, jsonify, redirect, url_for, flash
from forms import RegisterForm

app = Flask(__name__)  # file name
app.config['SECRET_KEY'] = 'thisisaverysecretivekey'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/menus')
def show_menu():
    return render_template('menus.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash('You have registered successfully.')
        return redirect(url_for('show_menu'))
    return render_template('register.html', form=form, errors=form.errors)


@app.route('/appointments')
def make_appointment():
    return 'You can make an appointment now.'


@app.route('/api/v1.0/services')
def get_services():
    services = ['Check up', 'Counseling', 'Special tests', 'Health & Wellness']
    return jsonify({'data': services})




app.run(debug=True)
