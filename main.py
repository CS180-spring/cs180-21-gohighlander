from flask import Flask, render_template, send_from_directory, session, redirect, url_for, request
import json

app = Flask(__name__)


# use session['logged_in'] boolean to verify login

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
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route("/api/login.php", methods=['POST'])
def loginphp():
    if session.get('logged_in'):
        return "logged_in"
    else:
        username = request.form['name'].lower()
        password = request.form['password']
        # check if username or password empty
        if not username or not password:
            return "Username or Password Empty"

        # check username
        with open('users.json', 'r') as f:
            users = json.load(f)

        if username in users:
            if users[username]['password'] == password:
                session['logged_in'] = True
                session['username'] = username
                session['permission'] = users[username]['permission']
                return "logged_in"
            else:
                return "Username or Password Wrong"
        else:
            return "Username or Password Wrong"


@app.route("/register.php")
def register():
    if session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('register.html')


@app.route("/api/register.php", methods=['POST'])
def registerphp():
    if session.get('logged_in'):
        return "success"
    else:
        # session['logged_in'] = True
        username = request.form['name'].lower()
        password = request.form['password']
        # check if username or password empty
        if not username or not password:
            return "Username or Password Empty"
        # check username
        with open('users.json', 'r') as f:
            users = json.load(f)

        if username not in users:
            users[username] = {}
            users[username]['password'] = password
            users[username]['permission'] = '0'  # 0 as regular user
            with open('users.json', 'w') as json_file:
                json.dump(users, json_file)
            return "success"
        else:
            return "User Exists"


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
    if session.get('logged_in'):
        with open('schedules.json', 'r') as f:
            schedules = json.load(f)
        if session['username'] in schedules:
            userScheduleCode = schedules[session['username']]
        else:
            userScheduleCode = ''
        return render_template("my_schedule.html", userScheduleCode=userScheduleCode)
    else:
        return redirect(url_for('login'))


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


@app.route("/api/get_users.php")
def getusersphp():
    if session.get('logged_in') and session.get('permission') == "1":
        with open('users.json', 'r') as f:
            usersJSON = json.load(f)
            users = []
            for user in usersJSON:
                users.append(user)
            return json.dumps(users)
    else:
        return "Unauthorized"


@app.route("/api/remove_user.php", methods=['GET'])
def removeuserphp():
    if session.get('logged_in') and session.get('permission') == "1":
        username = request.args.get('username')
        # prevent deleting self
        if username == session.get('username'):
            return "Can't delete your self"
        # get json
        with open('users.json', 'r') as f:
            usersJSON = json.load(f)

        with open('schedules.json', 'r') as f:
            scheduleJSON = json.load(f)
        # check if deleting user have >= permission
        if int(usersJSON[username]['permission']) >= int(session.get('permission')):
            return "Can not delete user with same permission or larger permission"
        # handle access violation
        if username in usersJSON:
            del usersJSON[username]
            # delete schedule
            if username in scheduleJSON:
                del scheduleJSON[username]
        else:
            return "Username Not Exist"
        # save it back
        with open('users.json', 'w') as json_file:
            json.dump(usersJSON, json_file)
        with open('schedules.json', 'w') as json_file:
            json.dump(scheduleJSON, json_file)

        return "success"

    else:
        return "Unauthorized"


@app.route("/api/change_password.php")
def changepasswordphp():
    if session.get('logged_in') and int(session.get('permission')) >= 1:
        username = request.args.get('username')
        password = request.args.get('password')
        if not username or not password:
            return "Missing parameters"

        with open('users.json', 'r') as f:
            usersJSON = json.load(f)
            #run checks
            if username not in usersJSON:
                return "User does not exist"

            if int(usersJSON[username]['permission']) >= int(session.get('permission')):
                return "Can not change user with same permission or larger permission"

            #do work
            usersJSON[username]['password'] = password

            # save it back
            with open('users.json', 'w') as json_file:
                json.dump(usersJSON, json_file)

            return "Operation Success"

    else:
        return "Unauthorized"

@app.route("/api/change_permission.php")
def changepermissionphp():
    if session.get('logged_in') and int(session.get('permission')) >= 1:
        username = request.args.get('username')
        permission = request.args.get('perm')
        if not username or not permission:
            return "Missing parameters"
        if not permission.isdigit():
            return "Wrong Parameter"

        with open('users.json', 'r') as f:
            usersJSON = json.load(f)
            #run checks
            if username not in usersJSON:
                return "User does not exist"

            if int(usersJSON[username]['permission']) >= int(session.get('permission')):
                return "Can not change user with same permission or larger permission"

            if int(permission) >= int(session.get('permission')):
                return "Can not change permission larger or equal to your current permission"

            #do work
            usersJSON[username]['permission'] = permission

            # save it back
            with open('users.json', 'w') as json_file:
                json.dump(usersJSON, json_file)

            return "Operation Success"

    else:
        return "Unauthorized"


@app.route("/parking.php")
def parking():
    if session.get('logged_in'):
        return render_template('parking.html')
    else:
        return redirect(url_for('login'))

@app.route('/static/parking.json')
def parkingjson():
    return send_from_directory(app.static_folder, 'parking.json')
    
@app.route("/admin")
def admin():
    if session.get('logged_in') and int(session.get('permission')) >= 1:
        return render_template('admin.html')
    else:
        return redirect(url_for('login'))

@app.route("/images/192x192.png")
def logo192():
    return send_from_directory(app.static_folder, '192x192.png')

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

@app.route("/api/admin_get_schedule.php", methods=['GET'])
def admin_get_schedule():
    username = request.args.get('username')
    if not username:
        return "Missing parameters"
    if session.get('logged_in') and int(session.get('permission')) >= 1:
        with open('schedules.json', 'r') as f:
            schedules = json.load(f)
        if username in schedules:
            userScheduleCode = schedules[username]
        else:
            userScheduleCode = ''
        return userScheduleCode
    else:
        return "Unauthorized"

#use eJyLjgUAARUAuQ== for empty schedule
@app.route("/api/admin_save_schedule.php", methods=['GET'])
def admin_save_schedulephp():
    username = request.args.get('username')
    scheduleHash = request.args.get('sh')
    if not username or not scheduleHash:
        return "Missing parameters"
    if session.get('logged_in') and int(session.get('permission')) >= 1:
        with open('schedules.json', 'r') as f:
            schedules = json.load(f)

        schedules[username] = scheduleHash

        with open('schedules.json', 'w') as json_file:
            json.dump(schedules, json_file)

        return "success"
    else:
        return "Unauthorized"

if __name__ == "__main__":
    app.secret_key = 'GoHighlanderAAA'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=3000)

