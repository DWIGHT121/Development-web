from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route('/')
@app.route('/basics')
def demo():
    return render_template("demo.html")

@app.route('/home')
def homepage():
    return render_template("homepage.html")

if(__name__)== "__main__":
    app.run(debug=True)
