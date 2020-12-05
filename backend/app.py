from flask import Flask, request, Response
from flask_json import FlaskJSON, as_json
from flask_cors import CORS
from datetime import datetime

import queries
import data

app = Flask(__name__)
FlaskJSON(app)
CORS(app)


# region GET /movies
@app.route('/movies', methods=["GET"])
def get_movies():
    return Response(queries.get_movies(), mimetype="application/json")


# endregion

# region GET /genres
@app.route('/genres', methods=["GET"])
def get_genres():
    return Response(queries.get_genres(), mimetype="application/json")


# endregion

# region POST /ratings/timestamp/bounds
@app.route("/ratings/timestamp/bounds", methods=["POST"])
@as_json
def get_ratings_timestamp_bounds():
    params = request.get_json()

    is_full = params.get("full", False)

    return queries.get_ratings_timestamp_bounds(is_full)


# endregion

# region POST /views
@app.route('/views', methods=["POST"])
@as_json
def get_views():
    print("==== Get view query ====")
    query = request.get_json()

    is_full = query.get("full", False)

    start = datetime.now()
    # Timing start
    if "filters" in query:
        filtered_views = queries.get_ratings_filtered(query["filters"], is_full).compute()
    else:
        filtered_views = data.ratings_big.compute() if is_full else data.ratings_small.compute()

    # Timing end
    end = datetime.now()
    duration = end - start
    print("Filter duration = " + str(duration))

    result = {}
    for grouping in query["queries"]:
        result[grouping] = queries.get_views(grouping, filtered_views)

    return result


# endregion

if __name__ == "__main__":
    app.run()
