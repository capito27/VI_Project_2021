from flask import Flask, jsonify
import numba

from datetime import date
import numpy as np
import pandas as pd

from data import ratings

app = Flask(__name__)


@app.route('/')
# @numba.jit(nopython=True, parallel=True)
def home():
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
        "data": np.zeros(12, dtype="Int64").tolist()
    }

    for rating in ratings:
        timestamp = rating.timestamp
        date_data = date.fromtimestamp(timestamp)
        values["data"][date_data.month - 1] += 1

    return jsonify(values)


if __name__ == "__main__":
    app.run()
