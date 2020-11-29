import sys


class Rating:
    def __init__(self, movieId: int, rating: float, timestamp: int):
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp
