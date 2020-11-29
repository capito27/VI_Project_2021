from datetime import datetime
from dask import dataframe as dd

data_root = "static/dataset/big/"
# data_root = "static/dataset/small/"

start = datetime.now()

ratings = dd.read_csv(data_root + "ratings.csv").compute()
movies = dd.read_csv(data_root + "movies.csv").compute()

end = datetime.now()

duration = end - start
print("Loading data duration = " + str(duration))

print("Ratings length: " + str(len(ratings)))
print("Movies length: " + str(len(movies)))
