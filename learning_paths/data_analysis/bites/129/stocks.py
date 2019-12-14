import requests
from collections import Counter, defaultdict

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    cap = cap.lstrip('$')
    if cap == 'n/a':
        return 0
    elif 'M' in cap:
        return float(cap.rstrip('M'))
    elif 'B' in cap:
        return float(cap.rstrip('B')) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    cap = 0
    for d in data:
        if d['industry'] == industry:
            cap += _cap_str_to_mln_float(d['cap'])
    return round(cap, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    stock_cap = dict()
    for d in data:
        stock_cap[d['symbol']] = _cap_str_to_mln_float(d['cap'])
    return max(stock_cap, key = stock_cap.get)


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sector_list = list()
    for d in data:
        sector_list.append(d['sector'])
    count = Counter(sector_list)
    del count['n/a']
    return (max(count, key = count.get), min(count, key = count.get))
    
    
