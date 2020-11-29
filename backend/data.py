from models import Rating
from datetime import datetime
import csv
import pandas as pd

# data_root = "static/dataset/big/"
data_root = "static/dataset/small/"

ratings_path = data_root + "ratings.csv"
ratings = []

ratings_raw = pd.read_csv("static/dataset/small/ratings.csv",
                          dtype={
                              "userId": "Int64",
                              "movieId": "Int64",
                              "rating": "Float64",
                              "timestamp": "Int64"},
                          engine="c", encoding="utf-8")

start = datetime.now()

for i, rating in ratings_raw.iterrows():
    ratings.append(Rating(
        int(rating.movieId),
        float(rating.rating),
        int(rating.timestamp)
    ))

# with open(ratings_path) as csvfile:
#     reader = csv.reader(csvfile, delimiter=",", quoting=csv.QUOTE_NONE)
#     next(reader)
#
#     for row in reader:
#         ratings.append(Rating(
#             int(row[1]),
#             float(row[2]),
#             int(row[3])
#         ))

end = datetime.now()

duration = end - start
print("Loading duration = " + str(duration))
print("Datas: " + str(len(ratings)))
