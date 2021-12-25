from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome!"

@app.route('/play/')
def play():
    return render_template('three.html')

@app.route('/play/<int:x>/')
def multiply (x):
    return render_template('vary.html', x = x)

@app.route('/play/<int:x>/<string:color>/')
def change (x, color):
    return render_template('color.html', x = x, color=color)

if __name__=="__main__":   
    app.run(debug=True)