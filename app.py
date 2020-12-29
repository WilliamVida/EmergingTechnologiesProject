from flask import Flask, request, render_template
import numpy as np
import csv
from numpy.polynomial.polynomial import polyfit
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd

import speedPowerModel

app = Flask(__name__)

def KNRegressor(input):
	dataset = pd.read_csv("powerproduction.csv")
	dataset.shape
	dataset.describe()

	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 1].values

	neigh = KNeighborsRegressor(n_neighbors = 2)
	neigh.fit(X, y)

	return neigh.predict([[input]])

@app.route("/")
def home():
	return app.send_static_file("index.html")

if __name == "__main__":
    app.run(debug=True, host="0.0.0.0")
