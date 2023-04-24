from flask import Flask, render_template, send_from_directory, session, redirect, url_for
import json

app = Flask(__name__)

#use session['logged_in'] boolean to verify login

@app.route("/")
def indexredir():
    return redirect(url_for('login'))


@app.route("/index.php")
def index():
    if session.get('logged_in'):
        return render_template("index.html")
    else:
        return redirect(url_for('login'))


# Define routes
@app.route("/api/check_session")
def check_session():
    if session.get('logged_in'):
        return "yes"
    else:
        return "no"


@app.route("/login.php")
def login():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('login.html')


@app.route('/logout.php')
def logout():
    return redirect(url_for('login'))


@app.route("/api/login.php", methods=['POST'])
def loginphp():
    return "logged_in"


@app.route("/register.php")
def register():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('register.html')


@app.route("/api/register.php", methods=['POST'])
def registerphp():
    return "success"


@app.route("/api/get_schedule.php", methods=['GET'])
def get_schedule():
    if session.get('logged_in'):
        with open('schedules.json', 'r') as f:
            schedules = json.load(f)
        if session['username'] in schedules:
            userScheduleCode = schedules[session['username']]
        else:
            userScheduleCode = ''
        return userScheduleCode
    else:
        return redirect(url_for('login'))


@app.route("/save_schedule.php")
def save_schedule():
    return render_template("save_schedule.html")


@app.route("/my_schedule.php")
def my_schedule():
    return render_template("my_schedule.html")


@app.route('/static/gzip.js')
def gzipjs():
    return send_from_directory(app.static_folder, 'gzip.js')

@app.route('/static/ics.js')
def icsjs():
    return send_from_directory(app.static_folder, 'ics.js')


@app.route("/api/save_schedule.php", methods=['POST'])
def save_schedulephp():
    if session.get('logged_in'):
        scheduleHash = request.form['sh']

        with open('schedules.json', 'r') as f:
            schedules = json.load(f)

        schedules[session['username']] = scheduleHash

        with open('schedules.json', 'w') as json_file:
            json.dump(schedules, json_file)

        return "success"
    else:
        return redirect(url_for('login'))


@app.route("/add_course.php")
def addcourse():
    if session.get('logged_in'):
        return render_template('term_selector.html')
    else:
        return redirect(url_for('login'))

@app.route("/course.php")
def courseadd():
    if session.get('logged_in'):
        return render_template('course_term.html')
    else:
        return redirect(url_for('login'))

@app.route("/manage_schedule.php")
def manageschedule():
    return render_template('manage_schedule.html')


if __name__ == "__main__":
    app.secret_key = 'GoHighlanderAAA'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=3000)
