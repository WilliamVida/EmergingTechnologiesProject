import numpy as np
import pandas as pd
from statistics import mean
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


# Linear regression function.
def LinearRegressionModel(speed):
	speedPower = pd.read_csv("powerproduction.csv").query("power > 0")
	speed = float(speed)

	X = speedPower.iloc[:, :-1].values
	y = speedPower.iloc[:, 1].values

	regressor = LinearRegression()
	regressor.fit(X, y)

	prediction = regressor.predict([[speed]])
	prediction = str(prediction[0])

	return prediction


# Polynomial regression function.
def PolynomialRegressionModel(speed):
	speedPower = pd.read_csv("powerproduction.csv").query("power > 0")
	speed = float(speed)

	X = speedPower.iloc[:, :-1].values
	y = speedPower.iloc[:, 1].values

	poly_reg = PolynomialFeatures(degree = 11)
	X_poly = poly_reg.fit_transform(X)
	pol_reg = LinearRegression()
	pol_reg.fit(X_poly, y)

	prediction = pol_reg.predict(poly_reg.fit_transform([[speed]]))
	prediction = str(prediction[0])

	return prediction


# K-nearest neighbours regression function.
def KNNRegressionModel(speed):
	speedPower = pd.read_csv("powerproduction.csv").query("power > 0")
	speed = float(speed)

	X = speedPower.iloc[:, :-1].values
	y = speedPower.iloc[:, 1].values

	neigh = KNeighborsRegressor(n_neighbors = 22)
	neigh.fit(X, y)

	prediction = neigh.predict([[speed]])
	prediction = str(prediction[0])

	return prediction
