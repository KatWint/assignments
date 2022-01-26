from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.userlogin import Members
from flask_app.models.user_info import Signup
from flask import Flask
from flask import flash
from flask_bcrypt import Bcrypt  
app=Flask(__name__)     
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Signup:
    db = 'LoginRegistration'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.userlogin = []

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM user_info;'
        results = connectToMySQL(cls.db).query_db(query)
        allRegistrations = []
        for row in results:
            registration = cls(row)
            allRegistrations.append(registration)
        return allRegistrations

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user_info (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());'
        return connectToMySQL(Members.db).query_db(query, data)

    @classmethod
    def from_registration_to_user( cls , data ):
        query = "SELECT * FROM user_info LEFT JOIN profiles ON UserLogin.Registration_id = registration.id WHERE registration.id = %(id)s;"
        results = connectToMySQL(Members.db).query_db( query , data )
        registrations = cls( results[0] )
        for row_from_db in results:
            user_data = {
                "id":row_from_db["profiles.id"],
                'email':row_from_db["profiles.email"]
            }
            Signup.Members.append( Members( user_data ) )
        return registrations

    @staticmethod
    def validate_registration(registration):
        is_valid = True 
        if len(registration['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(registration['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(registration['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(registration['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid

