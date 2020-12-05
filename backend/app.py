from flask import Flask, request, Response
from flask_json import FlaskJSON, as_json
from flask_cors import CORS
from datetime import datetime

import queries

app = Flask(__name__)
FlaskJSON(app)
CORS(app)


@app.route('/movies')
def get_movies():
    return Response(queries.get_movies(), mimetype="application/json")


@app.route('/genres')
def get_genres():
    return Response(queries.get_genres(), mimetype="application/json")


@app.route('/views', methods=["POST"])
@as_json
def get_views():
    print("==== Get view query ====")
    query = request.get_json()

    is_full = query.get("full", False)

    start = datetime.now()
    # Timing start

    filtered_views = queries.get_ratings_filtered(query["filters"], is_full).compute()

    # Timing end
    end = datetime.now()
    duration = end - start
    print("Filter duration = " + str(duration))

    result = {}
    for grouping in query["queries"]:
        result[grouping] = queries.get_views(grouping, filtered_views)

    return result


if __name__ == "__main__":
    app.run()
