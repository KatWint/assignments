from crypt import methods
from flask import Flask, render_template, request, redirect

from users import Users
app = Flask(__name__)


@app.route('/')
def index():
    return render_template ('read.html', all_users = Users.get_all())

@app.route('/create/')
def add_user():
    return render_template('create.html')

@app.route('/new_user/', methods = ['POST'])
def added_user():
    data = {
        'first name': request.form['first_name'],
        'last name':  request.form['last_name'],
        'email': request.form['email'],
        'created at': request.form['created_at']
    }
    Users.save(data)
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)
