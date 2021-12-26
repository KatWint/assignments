from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html')

@app.route ('/<int:x>')
def rows(x):
    return render_template('index2.html', x=x)

if __name__=="__main__":  
    app.run(debug=True)