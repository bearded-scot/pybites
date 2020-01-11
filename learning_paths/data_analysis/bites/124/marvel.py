from collections import Counter, namedtuple
import csv
import re
import operator

import requests

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex appearances year')


# csv parsing code provided so this Bite can focus on the parsing

def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode('utf-8')


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])




# start coding
characters = load_data()
def most_popular_characters(characters=characters, top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """
    char_app = list()
    for character in characters:
        x = character
        (n, a) = x.name, x.appearances
        char_app.append((n,a))
    top_n = [key for key, value in char_app][:top]
    return print(top_n)




def max_and_min_years_new_characters(characters=characters):
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv
       characters, or the 'year' attribute of the namedtuple, return a tuple
       of (max_year, min_year)
    """
    years = list()
    for character in characters:
        if len(character.year) == 4:
            years.append(character.year)
    char_count = Counter(years)
    char_count_ordered = {k: v for k, v in sorted(char_count.items(), key = lambda item: item[1], reverse = True)}
    return max(char_count_ordered.items(), key=operator.itemgetter(1))[0], min(char_count_ordered.items(), key=operator.itemgetter(1))[0]



def get_percentage_female_characters(characters=characters):
    """Get the percentage of female characters as percentage of all genders
       over all appearances.
       Ignore characters that don't have gender ('sex' attribue) set
       (in your characters data set you should only have Male, Female,
       Agender and Genderfluid Characters.
       Return the result rounded to 2 digits
    """
    gender_list = []
    pattern = re.compile(r'(\w+) (\w+)')
    for character in characters:
        if len(character.sex) > 0:
            gender_list.append(re.sub(pattern, r'\1', character.sex))
    gender_count = Counter(gender_list)
    total_gender_count = (gender_count['Male'] + gender_count['Female'] + gender_count['Agender'] + gender_count['Genderfluid'])
    return (gender_count['Female']/total_gender_count)*100


