from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask
from flask import flash
from flask_bcrypt import Bcrypt  
app=Flask(__name__)     
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Members:
    db = 'LoginRegistration'
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.password = data['password']
        self.updated_at = data['updated_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM profiles;'
        results = connectToMySQL(cls.db).query_db(query)
        allLogins = []
        for row in results:
            ulogins = cls(row)
            allLogins.append(ulogins)
        return allLogins

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM profiles WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO profiles (email, password, updated_at) VALUES (%(name)s,%(password)s, NOW());'
        return connectToMySQL(cls.db).query_db(query, data)
