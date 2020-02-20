NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

PY_CONTENT_CREATORS = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']

def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return [name.title() for name in set(names)]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key = lambda x: x.split(' ')[1], reverse = True)




def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    return min(names, key=lambda x: len(x.split(' ')[0])).split(' ')[0]


print(dedup_and_title_case_names(NAMES))
print(shortest_first_name(PY_CONTENT_CREATORS))