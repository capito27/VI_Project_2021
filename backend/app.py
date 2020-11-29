from flask import Flask, jsonify
import numpy as np

from data import ratings

app = Flask(__name__)


def test():
    data = np.zeros(12)

    months = ratings.timestamp // 2629743 % 12
    for i in range(0, 12):
        data[i] = len(months[months == i])

    return data


@app.route('/')
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
        "data": test().tolist()
    }

    return jsonify(values)


if __name__ == "__main__":
    app.run()
