import flask as fl
import numpy as np
import csv
from numpy.polynomial.polynomial import polyfit
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import tensorflow.keras as kr
import json
from flask import Flask, redirect, url_for, request

from speedPowerModel import KNRegressor

app = fl.Flask(__name__)

@app.route("/")
def home():
	return app.send_static_file("index.html")
	
@app.route("/api/input/<speed>")
def KNReg(speed):
	prediction = KNRegressor(speed)

	return {"prediction is ", prediction}

@app.route('/api/uniform')
def uniform():
	return {"value": 500}

@app.route('/api/normal')
def normal():
	return {"value": np.random.normal()}

if __name__ == "__main__":
    app.run(debug = True)
