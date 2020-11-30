from datetime import datetime
from dask import dataframe
import dask

data_root = "static/dataset/big/"
# data_root = "static/dataset/small/"

start = datetime.now()

ratings = dataframe.read_csv(data_root + "ratings.csv").compute()
movies = dataframe.read_csv(data_root + "movies.csv").compute()

end = datetime.now()

duration = end - start
print("Loading data duration = " + str(duration))

print("Ratings length: " + str(len(ratings)))
print("Movies length: " + str(len(movies)))

