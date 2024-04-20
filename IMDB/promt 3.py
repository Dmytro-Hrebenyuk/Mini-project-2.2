"""find film"""
def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    '''
    Returns a set of all keywords associated with the given film_name
    in the film_keywords dictionary.
    >>> find_film_keywords({'drummer': ['Wild in the Streets', 'Whiplash (2014)',\
          'Wittercism (2012)'],
    ...                     'bounty-hunter': ['Ben 10', \
    '"Dog the Bounty Hunter" (2003)', 'The Hateful Eight (2015)']},
    ...                    'Whiplash (2014)')
    {'drummer'}
    '''
    return {keyword for keyword, films in film_keywords.items() if film_name in films}


def find_films_with_keywords(film_keywords: dict, num_of_films: int) -> list:
    """
    Returns the set of all keywords used in the movie film_name.
    >>> find_films_with_keywords({'horror': ('name1', 'name2', 'name3'),
    ...                            'comedy': ('name1', 'name2', 'name4'),
    ...                            'detective': ('name1', 'name1')}, 2)
    [('name1', 4), ('name2', 2)]
    """
    film_counts = {}
    for films in film_keywords.values():
        for film in films:
            film_counts[film] = film_counts.get(film, 0) + 1

    result = sorted(film_counts.items(), \
                    key=lambda x: (-x[1], x[0]))[:num_of_films] if num_of_films > 0 else []
    return result
