from flask import Flask, jsonify
import numba

from datetime import date
import numpy as np
import pandas as pd

from data import ratings

app = Flask(__name__)

@app.route('/')
#@numba.jit(nopython=True, parallel=True)
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
    months = ratings.timestamp // 2629743 % 12
    for i in range(0,12):
    	values["data"][i] = len(months[months == i])
    	print(values["data"][i])

    return jsonify(values)


if __name__ == "__main__":
    app.run()
