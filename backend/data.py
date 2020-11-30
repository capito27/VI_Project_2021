from datetime import datetime
import numpy as np
import pandas as pd
import dask
import dask.dataframe as df

# data_root = "static/dataset/big/"
data_root = "static/dataset/small/"

print("==== Start loading ====")
start = datetime.now()
# Loading start

# Loading ratings
ratings_dtypes = {
    "movieId": int,
    "rating": float,
    "timestamp": int,
}
ratings = df.read_csv(data_root + "ratings.csv", usecols=[1, 2, 3], dtype=ratings_dtypes)

# Processing ratings
ratings.timestamp = df.map_partitions(pd.to_datetime, ratings.timestamp, unit="s")
ratings["month"] = ratings.timestamp.dt.month
ratings["week"] = ratings.timestamp.dt.isocalendar().week
ratings["day_of_week"] = ratings.timestamp.dt.dayofweek


# Loading movies
movies = df.read_csv(data_root + "movies.csv")

# Loading end
end = datetime.now()
duration = end - start
print("Loading data duration = " + str(duration))
print("==== End loading ====")


print("==== Start Testing ====")
start = datetime.now()
# Testing start

print("Ratings length: " + str(len(ratings)))
print("Movies length: " + str(len(movies)))

print(ratings.dtypes)
print(ratings.head())

# Testing end
end = datetime.now()
duration = end - start
print("Testing duration = " + str(duration))
print("==== End Testing ====")
