import flask as fl
from flask import Flask, redirect, url_for, request, jsonify
import tensorflow.keras as kr
from speedPowerModel import LinearRegressionModel, PolynomialRegressionModel, KNNRegressionModel

app = fl.Flask(__name__)


# Add root route.
@app.route("/")
def home():
    return app.send_static_file("index.html")


# Route for linear regression.
@app.route("/api/linear/<speed>")
def LinearPrediction(speed):
    if float(speed) == 0:
        return jsonify({"value": 0})

    prediction = LinearRegressionModel(speed)

    return jsonify({"value": prediction})


# Route for polynomial regression.
@app.route("/api/polynomial/<speed>")
def PolynomialPrediction(speed):
    if float(speed) == 0:
        return jsonify({"value": 0})

    prediction = PolynomialRegressionModel(speed)

    return jsonify({"value": prediction})


# Route for k-nearest neighbours regression.
@app.route("/api/knn/<speed>")
def KNNPrediction(speed):
    if float(speed) == 0:
        return jsonify({"value": 0})

    prediction = KNNRegressionModel(speed)

    return jsonify({"value": prediction})


# Route for neural network.
@app.route("/api/nn/<speed>")
def NeuralNetworkPrediction(speed):
    if float(speed) == 0:
        return jsonify({"value": 0})

    speed = float(speed)
    model = kr.models.load_model("model.h5")
    prediction = model.predict([speed])

    return jsonify({"value": prediction.item(0)})


if __name__ == "__main__":
    app.run(debug=True)
