"""find films"""
from collections import Counter

def find_film_keywords(film_keywords, film_name):
    '''
    Returns a set of all keywords associated with the given film_name\
 in the film_keywords dictionary.

    >>> find_film_keywords({'drummer':['Wild in the Streets',\
'Whiplash (2014)','Wittercism (2012)'],\
'bounty-hunter':['Ben 10','"Dog the Bounty Hunter"\
 (2003)','The Hateful Eight (2015)']},'Whiplash (2014)') == {'drummer'}
    True
    '''
    return set(keyword for keyword, films in film_keywords.items() if film_name in films)


def find_films_with_keywords(film_keywords, num):
    """
    Returns a list of films with the most keywords.

    >>> find_films_with_keywords({'horor': ('name1', 'name2', 'name3'), \
    'comedy': ('name1', 'name2' , 'name4'), 'detective': ('name1', 'name1')}, 2)
    [('name1', 4), ('name2', 2)]
    """
    film_counts = Counter(film for films in film_keywords.values() for film in films)
    sorted_films = sorted(film_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_films[:num] if num > 0 else []
