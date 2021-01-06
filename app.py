import flask as fl
import numpy as np
import csv
from numpy.polynomial.polynomial import polyfit
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import tensorflow.keras as kr
import json
from flask import Flask, redirect, url_for, request, jsonify

from speedPowerModel import LinearRegressionModel, PolynomialRegressionModel, KNNRegressionModel

app = fl.Flask(__name__)

@app.route("/")
def home():
	return app.send_static_file("index.html")
	
@app.route("/api/linear/<speed>")
def LinearPrediction(speed):
	if (float(speed) == 0):
		return jsonify({"value": 0})
	
	prediction = LinearRegressionModel(speed)
	
	return jsonify({"value": prediction})
	
@app.route("/api/polynomial/<speed>")
def PolynomialPrediction(speed):
	if (float(speed) == 0):
		return jsonify({"value": 0})
	
	prediction = PolynomialRegressionModel(speed)
	
	return jsonify({"value": prediction})

@app.route("/api/knn/<speed>")
def KNNPrediction(speed):
	if (float(speed) == 0):
		return jsonify({"value": 0})
	
	prediction = KNNRegressionModel(speed)
	
	return jsonify({"value": prediction})

@app.route("/api/nn/<speed>")
def NeuralNetworkPrediction(speed):
	if (float(speed) == 0):
		return jsonify({"value": 0})
	
	speed = float(speed)
	model = kr.models.load_model('model.h5')
	prediction = model.predict([speed])
	
	return jsonify({"value": prediction.item(0)})

if __name__ == "__main__":
    app.run(debug = True)
