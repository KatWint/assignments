from crypt import methods
from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.user_info import Signup
from flask_app.models.userlogin import Members




@app.route('/')
def index():
    return redirect ('/home')

from flask_bcrypt import Bcrypt 
app=Flask(__name__)      
bcrypt = Bcrypt(app)

@app.route('/register', methods=['POST'])
def register():
    if not Signup.validate_user(request.form):
        return redirect('/home')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = Signup.save(data)
    session['user_id'] = user_id
    return redirect('/welcome')



