from flask import Flask, render_template
# may not need pandas in this file, unsure at the moment
# import pandas as pd
# below is for the transferred file(s) that handles the data analysis (converted Jupyter notebook scripts)
import CHARTizard as analysis
import CHARTizard2 as analysis2

app = Flask(__name__)

data_file = './static/data/pokemon.csv'

@app.route('/')
def index():
  return render_template('index.html', data=analysis.export(data_file), dat=analysis2.export(data_file))