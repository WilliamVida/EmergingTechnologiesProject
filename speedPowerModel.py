import numpy as np
import pandas as pd
from statistics import mean
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def LinearRegressionModel(speed):
	speedPower = pd.read_csv("powerproduction.csv").query("power > 0")
	speed = float(speed)

	X = speedPower.iloc[:, :-1].values
	y = speedPower.iloc[:, 1].values

	(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size = 0.8, random_state = 0)

	regressor = LinearRegression()
	regressor.fit(X_train, y_train)

	prediction = regressor.predict([[speed]])
	prediction = str(prediction[0])

	return prediction


def PolynomialRegressionModel(speed):
	speedPower = pd.read_csv("powerproduction.csv").query("power > 0")
	speed = float(speed)

	X = speedPower.iloc[:, :-1].values
	y = speedPower.iloc[:, 1].values

	poly_reg = PolynomialFeatures(degree = 17)
	X_poly = poly_reg.fit_transform(X)
	pol_reg = LinearRegression()
	pol_reg.fit(X_poly, y)

	prediction = pol_reg.predict(poly_reg.fit_transform([[speed]]))
	prediction = str(prediction[0])

	return prediction


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
