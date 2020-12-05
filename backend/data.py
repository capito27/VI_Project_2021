from datetime import datetime
import numpy as np
import pandas as pd
import dask
import dask.dataframe as df

# Set tp true to have big dataset
load_full = False

# region General variables
small_data_root = "static/dataset/small/"
big_data_root = "static/dataset/big/"

# Ratings
ratings_filename = "ratings.csv"
ratings_dtypes = {
    "movieId": int,
    "rating": float,
    "timestamp": int,
}
ratings_cols = [1, 2, 3]

# Ratings
movies_filename = "movies.csv"
movies_dtypes = {
    "movieId": int,
    "title": str,
    "genres": str,
}
movies_cols = [0, 1, 2]
# endregion

# region Data loading
print("==== Start loading small ====")
start = datetime.now()
# Loading start

ratings_small = df.read_csv(small_data_root + ratings_filename, usecols=ratings_cols, dtype=ratings_dtypes)
movies_small = df.read_csv(small_data_root + movies_filename, usecols=movies_cols, dtype=movies_dtypes)

# Loading end
end = datetime.now()
duration = end - start
print("Loading small dataset duration = " + str(duration))
print("==== End loading small ====")

print("==== Start loading big ====")
start = datetime.now()
# Loading start

if load_full:
    ratings_big = df.read_csv(big_data_root + ratings_filename, usecols=ratings_cols, dtype=ratings_dtypes)
    movies_big = df.read_csv(big_data_root + movies_filename, usecols=movies_cols, dtype=movies_dtypes)

# Loading end
end = datetime.now()
duration = end - start
print("Loading big dataset duration = " + str(duration))
print("==== End loading big ====")
# endregion

# region Data processing
print("==== Processing small ====")
start = datetime.now()
# Loading start

ratings_small.timestamp = df.map_partitions(pd.to_datetime, ratings_small.timestamp, unit="s")
ratings_small["month"] = ratings_small.timestamp.dt.month
ratings_small["week"] = ratings_small.timestamp.dt.isocalendar().week
ratings_small["day_of_week"] = ratings_small.timestamp.dt.dayofweek
ratings_small["day_of_month"] = ratings_small.timestamp.dt.day

movies_small["genres_array"] = movies_small.genres.str.split("|")

print("Small ratings length: " + str(len(ratings_small)))
print("Small movies length: " + str(len(movies_small)))

# Loading end
end = datetime.now()
duration = end - start
print("Processing small dataset duration = " + str(duration))
print("==== End processing small ====")

print("==== Processing big ====")
start = datetime.now()
# Loading start

if load_full:
    ratings_big.timestamp = df.map_partitions(pd.to_datetime, ratings_big.timestamp, unit="s")
    ratings_big["month"] = ratings_big.timestamp.dt.month
    ratings_big["week"] = ratings_big.timestamp.dt.isocalendar().week
    ratings_big["day_of_week"] = ratings_big.timestamp.dt.dayofweek
    ratings_big["day_of_month"] = ratings_big.timestamp.dt.day

    movies_big["genres_array"] = movies_big.genres.str.split("|")

    genres = movies_big["genres_array"].explode().unique().compute()

    print("Big ratings length: " + str(len(ratings_big)))
    print("Big movies length: " + str(len(movies_big)))

# Loading end
end = datetime.now()
duration = end - start
print("Processing big dataset duration = " + str(duration))
print("==== Processing big ====")
# endregion

# region Testing
print("==== Start Testing ====")
start = datetime.now()
# Testing start


# Testing end
end = datetime.now()
duration = end - start
print("Testing duration = " + str(duration))
print("==== End Testing ====")
# endregion
