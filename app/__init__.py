from flask import Flask, render_template, jsonify, request

app = Flask(__name__)  # file name


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/menus')
def show_menu():
    return render_template('menus.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    print(request.method)
    if request.method == 'POST':
        errors = []
        name = request.form.get('name')
        email = request.form.get('email')
        if not name:
            errors.append('You need to enter your name.')
        if not email:
            errors.append('You need to enter an email.')
        return render_template('register.html', errors=errors)
    return render_template('register.html')


@app.route('/appointments')
def make_appointment():
    return 'You can make an appointment now.'


@app.route('/api/v1.0/services')
def get_services():
    services = ['Check up', 'Counseling', 'Special tests', 'Health & Wellness']
    return jsonify({'data': services})




app.run(debug=True)
