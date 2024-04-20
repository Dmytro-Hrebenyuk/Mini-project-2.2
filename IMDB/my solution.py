"""
This module is about work with IMDB.
"""
def find_film_keywords(film_keywords: dict, film_name: str):
    '''
    Returns a set of all keywords associated with the given film_name\
 in the film_keywords dictionary.
    >>> find_film_keywords({'drummer':['Wild in the Streets',\
'Whiplash (2014)','Wittercism (2012)'],\
'bounty-hunter':['Ben 10','"Dog the Bounty Hunter"\
 (2003)','The Hateful Eight (2015)']},'Whiplash (2014)') == {'drummer'}
    True
    '''
    keywords_set = set()

    for keyword, films in film_keywords.items():
        if film_name in films:
            keywords_set.add(keyword)

    return keywords_set


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    Returns the set of all keywords used in the movie film_name.
    >>> find_films_with_keywords({'horor': ('name1', 'name2', 'name3'), \
    'comedy': ('name1', 'name2' , 'name4'), 'detective': ('name1', 'name1')}, 2)
    [('name1', 4), ('name2', 2)]

    """
    film_counts = {}
    for films in film_keywords.values():
        for film in films:
            if film in film_counts:
                film_counts[film] += 1
            else:
                film_counts[film] = 1
    films_with_keywords = list(film_counts.items())
    films_with_keywords.sort(key=lambda x: (-x[1], x[0]))
    result = films_with_keywords[:num_of_films] if num_of_films > 0 else []
    return result
