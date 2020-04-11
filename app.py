from flask import Flask, render_template
from flask_frozen import Freezer
# from myapplication import app

app = Flask(__name__)


freezer = Freezer(app)


@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/chartizard.html')
def chartizard():
	return render_template('chartizard.html')

if __name__ == '__main__':
    freezer.freeze()