from flask import Flask, request, Response
from flask_json import FlaskJSON, as_json
from flask_cors import CORS

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
    query = request.get_json()

    filtered_views = queries.get_ratings_filtered(query["filters"])

    result = {}
    for grouping in query["queries"]:
        result[grouping] = queries.get_views(grouping, filtered_views)

    return result


if __name__ == "__main__":
    app.run()
