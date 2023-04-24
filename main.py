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
    return "eJzFlm1v2kgQx7/KyG/ak3zgtYOboFxUYtwEFQzCzqH21BeLvcR7MV60aytHTv3unYUQDCT0AaK+QTszyzA7v/3P8s//RixKqZjR1KtMSKNpyNvxW8sEl5hA3MYfhmkkTMWSzwoucoxHvncddLxWF7x+r3ejl1GnH4S4cZks4kWGGQ0/uBqSU2sEf4JlEQyPS54lPL/F2JWQichhRIs7niu4plmGG6QQUwwSy7LQKuYznabL4qKUDB0TGpdZMQ/olCkMDCSfUjmHTq4KWcaFkE04p5BKNvnrzZTyrBBNlVIp8vH7MpY1lpRvLuCylIXITQgXkfM6vTgfy/rF3ixjkee8ditpSqeVVFcLhwmXOrzOhJXiKSY0UwwPYTQxLS7u16505Zs8+VTEp/qw5N3i6GxlntraVG1aaNM6qVtO3bZsR+9ZOd26dbZyLgkE5XTMZAWBzsHiJ/cjjkRhdcaoFelmM6lbH84kAoJFtq9fzZfuh2vDGQFyQo50PWx383pgGaLMtq6F7bgn62sxEvJOpWL2evdim+Pj6n5FT3N89D0D8tSpgrTJ64BcNm4JMhwMfxrkPqF3gmjYb994Gh9EfQj7H6JRa+gDFtMJfH/YCa52qHohlvmc4nt4SMmxSRDGHGiegJ/f8pwxXWdF+8Q9kvQfUv4vp7WHlIoK5s9omvipY2vIj0C/x3jpe0LsbGrVaRyEeNG5fULthf4xhTpAfl5n0PVD6H+AkX8Jbf9vv9sf9Pwgeo4rWXC1t7i2solkCfRqOAbnMdse5SfvSIUnHQtJkdb815BmM0U59qTCc4CejJrQLeN4P9DK9H1ZtY1NpO7BSMkOUruC9LL/6bp7TKjtTugN/ciHMBqicm+G/u7g1VWRBcrG1tQtyoTlBYTYS6YUeGhgzesBXNVmm6u4VEr/7C+xpHEquOU0Kiw99JjQyth/OB6Y3D+Dn8W5JVD36DTJDs1GZQCH3jFZHjZ/f6dOFW5NNnXaQw+OXP3AxqIoDlcq2WRrv8LwPVyp+57Xn5Lq9mv6Xak6jSM9oyxjOa1h/CHFZaHu6HumQ7U127ASNMHXX/ix/9V3XLc6Y/PavcgmldsyQtOEj6vw9n/rH3yud4a78+rjoPpe7xkHX74B9ZAVcA=="


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
    return "success"


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
