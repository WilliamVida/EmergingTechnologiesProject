import flask as fl
import numpy as np
import csv
from numpy.polynomial.polynomial import polyfit
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import tensorflow.keras as kr
import json

import speedPowerModel

app = fl.Flask(__name__)

@app.route("/")
def home():
	return app.send_static_file("index.html")

@app.route("/api/power/<input>")
def KNRegressor(speed):
	dataset = pd.read_csv("powerproduction.csv")
	dataset.shape
	dataset.describe()

	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 1].values

	neigh = KNeighborsRegressor(n_neighbors = 2)
	neigh.fit(X, y)

	return neigh.predict([[input]])

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/getmethod/<jsdata>')
def get_javascript_data(jsdata):
    return jsdata