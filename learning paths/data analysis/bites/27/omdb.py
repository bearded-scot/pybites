import glob
import json
import os
from urllib.request import urlretrieve
import re

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movie_list = list()
    for file in files:
        with open(file) as movie:
            movie_list.append(json.loads(movie.read()))
    return movie_list


def get_single_comedy(movies):
    return [movie['Title'] for movie in movies if 'Comedy' in movie['Genre']][0]
    

def get_movie_most_nominations(movies):
    nominations = dict()
    for movie in movies:
        nominations[movie['Title']] = int(re.sub(r'.* (\d+) nominat.*', r'\1', movie['Awards']))
    return max(nominations, key = lambda k: nominations[k])


def get_movie_longest_runtime(movies):
    runtimes = dict()
    for movie in movies:
        runtimes[movie['Title']] = int(re.sub(r'(\d+) min.*', r'\1', movie['Runtime']))
    return max(runtimes, key = lambda k: runtimes[k])
