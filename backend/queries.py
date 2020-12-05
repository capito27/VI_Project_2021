from flask import jsonify
import numpy as np

import data


########################
# Processing
def get_ratings_filtered(filter_list):
    movies_conditions = get_movies_genres_conditions(True, filter_list["genres"])

    if isinstance(movies_conditions, bool):
        return data.ratings

    return data.ratings.where(
        data.ratings.movieId.isin(
            data.movies.movieId.where(movies_conditions).dropna().compute()
        )
    )


def get_views_groupby(column, ratings):
    return ratings[[column, "movieId"]].groupby(column).count().compute()


def get_movies_genres_conditions(previous_condition, genre_conditions):
    for key, val in genre_conditions.items():
        if val:
            previous_condition &= data.movies.genres.str.contains(key)
        else:
            previous_condition &= ~data.movies.genres.str.contains(key)

    return previous_condition


########################
# Data queries
def get_movies():
    return data.movies[["movieId", "title"]].compute().to_json(orient="records")


def get_genres():
    return data.genres.to_json(orient="records")


def get_views(to_groupby, ratings=data.ratings):
    if to_groupby == "month":
        return views_per_month(ratings)
    elif to_groupby == "week":
        return views_per_week(ratings)
    elif to_groupby == "day":
        return "Unsupported"
    elif to_groupby == "dayofmonth":
        return "Unsupported"
    elif to_groupby == "dayofweek":
        return views_per_day_of_week(ratings)
    else:
        return "Unsupported"


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
