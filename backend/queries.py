from flask import jsonify
import numpy as np
from datetime import datetime

import data


# region == Processing
def get_ratings_filtered(filter_list, full=False):
    if full and data.load_full:
        ratings = data.ratings_big
        movies = data.movies_big
    else:
        ratings = data.ratings_small
        movies = data.movies_small

    movies_conditions = get_movies_genres_conditions(True, filter_list["genres"], movies)

    if isinstance(movies_conditions, bool):
        return ratings

    return ratings.where(
        ratings.movieId.isin(
            movies.movieId.where(movies_conditions).dropna().compute()
        )
    )


def get_views_groupby(column, ratings):
    return ratings[[column, "movieId"]].groupby(column).count()


def get_movies_genres_conditions(previous_condition, genre_conditions, movies):
    for key, val in genre_conditions.items():
        if val:
            previous_condition &= movies.genres.str.contains(key)
        else:
            previous_condition &= ~movies.genres.str.contains(key)

    return previous_condition


# endregion

# region == Queries
def get_movies(full=False):
    if full:
        return data.movies_big[["movieId", "title"]].compute().to_json(orient="records")
    return data.movies_small[["movieId", "title"]].compute().to_json(orient="records")


def get_genres():
    return data.genres.to_json(orient="records")


def get_views(to_groupby, ratings):
    start = datetime.now()
    # Timing start

    if to_groupby == "month":
        result = views_per_month(ratings)
    elif to_groupby == "week":
        result = views_per_week(ratings)
    elif to_groupby == "day":
        result = "Unsupported"
    elif to_groupby == "dayofmonth":
        result = views_per_day_of_month(ratings)
    elif to_groupby == "dayofweek":
        result = views_per_day_of_week(ratings)
    else:
        result = "Unsupported"

    # Timing end
    end = datetime.now()
    duration = end - start
    print(to_groupby + " duration = " + str(duration))

    return result


def views_per_month(ratings):
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

    month = get_views_groupby("month", ratings).reindex(np.arange(1, 13), fill_value=0)

    for i in range(0, 12):
        values["data"][i] = int(month.loc[i + 1].iloc[0])

    return values


def views_per_week(ratings):
    values = {
        "labels": np.arange(1, 53).tolist(),
        "data": np.zeros(52).tolist()
    }

    weeks = get_views_groupby("week", ratings).reindex(np.arange(1, 54), fill_value=0)

    for i in range(0, 52):
        values["data"][i] = int(weeks.loc[i + 1].iloc[0])
    values["data"][0] += int(weeks.loc[53].iloc[0])

    return values


def views_per_day_of_month(ratings):
    values = {
        "labels": np.arange(1, 32).tolist(),
        "data": np.zeros(31).tolist()
    }

    days = get_views_groupby("day_of_month", ratings).reindex(np.arange(1, 32), fill_value=0)

    for i in range(0, 31):
        values["data"][i] = int(days.loc[i + 1].iloc[0])

    return values


def views_per_day_of_week(ratings):
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

    day_of_week = get_views_groupby("day_of_week", ratings).reindex(np.arange(1, 8), fill_value=0)

    for i in range(0, 7):
        values["data"][i] = int(day_of_week.loc[i + 1].iloc[0])

    return values
# endregion
