import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import statistics as st
import operator

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    movie_dict = defaultdict(list)
    with open(MOVIE_DATA) as movies:
        reader = csv.DictReader(movies)
        for row in reader:
            if row['title_year'] != '' and int(row.get('title_year'.strip())) >= 1960:
                movie_dict[row['director_name']].append(Movie(row['movie_title'].strip(), int(row['title_year']), float(row['imdb_score'])))
    return movie_dict

def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = list()
    for movie in movies:
        scores.append(movie.score)
    return round(st.mean(scores),1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    avg_scores = list()
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            avg_scores.append((director, calc_mean_score(movies)))
    return sorted(avg_scores, key = operator.itemgetter(1), reverse = True)
