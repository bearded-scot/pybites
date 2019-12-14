import os
import urllib.request
from collections import Counter
import re

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_stopwords():
    with open(stopwords_file) as stop_file:
        return [line.strip('\n').lower() for line in stop_file]

def get_harry_most_common_word():
    stopwords = get_stopwords()
    word_list = list()
    with open(harry_text) as harry:
        for line in harry.readlines():
            words = line.split()
            for word in words:
                word = re.sub(r'\W', '', word).lower()
                if word.strip() not in stopwords and len(word) > 1:
                    word_list.append(word.strip())
    word_count = Counter(word_list)
    return word_count.most_common(1)[0]
