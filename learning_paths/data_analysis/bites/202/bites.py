import csv
import os
from pathlib import Path
from urllib.request import urlretrieve
import re


data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)

pattern = re.compile(r'.*Bite (\d*).+;(.*)$')

def get_most_complex_bites(N=6, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    bites = dict()
    ret = list()
    with open(stats) as fin:
        reader = csv.reader(fin)
        next(reader)
        for line in reader:
            if len(line) > 1:
                line = ''.join(line)
            line = str(line)
            bites[re.sub(pattern, r'\1', line)] = re.sub(pattern, r'\2', line.strip("']"))
    ordered_bites = {k: v for k, v in sorted(bites.items(), key=lambda item: item[1], reverse=True)}
    for key, value in ordered_bites.items():
        if len(ret) < N:
            if value != 'None':
                ret.append(key)
    return ret


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)