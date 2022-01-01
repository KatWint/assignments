from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "make it happen capn"

@app.route('/', methods=['GET', 'POST'])
def index():
    session['number'] += 1
    return render_template('index.html')


@app.route('/destroy_session')
def redo():
    session.clear()
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)

