from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from dask import dataframe as df

from data import ratings, movies

app = Flask(__name__)
CORS(app)


@app.route('/views/per_month')
def views_per_month():
    values = {
        "labels": [
            "January",
            "February",
            "March",
            "April",
            "Mai",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        "data": np.zeros(12).tolist()
    }

    month = ratings[["month", "movieId"]].groupby("month").count().compute().to_numpy().tolist()

    for i in range(0, 12):
        values["data"][i] = month[i][0]

    return jsonify(values)


@app.route('/views/per_week')
def views_per_week():
    values = {
        "labels": np.arange(1, 53).tolist(),
        "data": np.zeros(52).tolist()
    }

    weeks = ratings[["week", "movieId"]].groupby("week").count().compute().to_numpy().tolist()

    for i in range(0, 52):
        values["data"][i] = weeks[i][0]
    values["data"][0] = weeks[52]

    return jsonify(values)


@app.route('/views/per_day')
def views_per_day():
    values = {
        "labels": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ],
        "data": np.zeros(7).tolist()
    }

    day_of_week = ratings[["day_of_week", "movieId"]].groupby("day_of_week").count().compute().to_numpy().tolist()

    for i in range(0, 7):
        values["data"][i] = day_of_week[i][0]

    return jsonify(values)


if __name__ == "__main__":
    app.run()
