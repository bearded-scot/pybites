from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    makers = list()
    for car in data:
        if year in car.values():
            makers.append(car["automaker"])
    count = Counter(makers)
    return max(count, key = count.get)


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = list()
    for car in data:
        if automaker in car.values() and year in car.values():
            models.append(car["model"])
    return set(models)
