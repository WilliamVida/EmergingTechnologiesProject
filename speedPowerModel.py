import numpy as np
import statsmodels.stats.weightstats as stat
import scipy.stats as ss
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv
from numpy.polynomial.polynomial import polyfit
from statistics import mean
import sklearn.cluster as skcl

def KNRegressor(input):
	dataset = pd.read_csv("powerproduction.csv")
	dataset.shape
	dataset.describe()

	X = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 1].values

	from sklearn.neighbors import KNeighborsRegressor
	neigh = KNeighborsRegressor(n_neighbors = 2)
	neigh.fit(X, y)

	return neigh.predict([[input]])
