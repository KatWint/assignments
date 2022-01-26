from crypt import methods
from flask_app import app
from flask import Flask, render_template, redirect, session, request, flash
from flask_app.models.user_info import Signup
from flask_app.models.userlogin import Members

from flask_bcrypt import Bcrypt  
app=Flask(__name__)    
bcrypt = Bcrypt(app)

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = Members.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/home")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/home')
    session['user_id'] = user_in_db.id
    return redirect("/logged_in")

@app.route ('/welcome')
def view_acct():
    return render_template('logged_in.html')
