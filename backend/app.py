from flask import Flask, jsonify
import numpy as np
import pandas as pd
from dask import dataframe as ddf

from data import ratings, movies

app = Flask(__name__)


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

    months = ratings.timestamp // 2629743 % 12
    for i in range(0, 12):
        values["data"][i] = len(months[months == i])

    return jsonify(values)


@app.route('/views/per_week')
def views_per_week():
    values = {
        "labels": np.arange(1, 53).tolist(),
        "data": np.zeros(52).tolist()
    }

    weeks = ratings.timestamp // 86400 // 7 % 52
    for i in range(0, 52):
        values["data"][i] = len(weeks[weeks == i])

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

    day_of_week = ddf.map_partitions(
        lambda df: pd.to_datetime(df.timestamp, unit="s").dt.dayofweek, ratings
    )

    for i in range(0, 7):
        values["data"][i] = len(day_of_week[day_of_week == i])

    return jsonify(values)


if __name__ == "__main__":
    app.run()