from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hi(name):
    print (name)
    return (f'Hi, ' + name,'!')

@app.route('/repeat/<int:num>/<name>')
def repeat(name, num):
    return name * num

if __name__=="__main__":
    app.run(debug=True)    




