from datetime import datetime
from dask import dataframe as dd

start = datetime.now()
ratings = dd.read_csv("static/dataset/big/ratings.csv")

end = datetime.now()

duration = end - start
print("Loading duration = " + str(duration))

print("Datas: " + str(len(ratings)))
