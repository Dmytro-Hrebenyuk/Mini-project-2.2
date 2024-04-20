"""find film"""
def find_film_keywords(film_keywords: dict, film_name: str) -> set:
    '''
    Returns a set of all keywords associated with the given film_name\
 in the film_keywords dictionary.
    >>> find_film_keywords({'drummer':['Wild in the Streets',\
'Whiplash (2014)','Wittercism (2012)'],\
'bounty-hunter':['Ben 10','"Dog the Bounty Hunter"\
 (2003)','The Hateful Eight (2015)']},'Whiplash (2014)') == {'drummer'}
    True
    '''
    return {keyword for keyword, films in film_keywords.items() if film_name in films}

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    Returns the set of all keywords used in the movie film_name.
    >>> find_films_with_keywords({'horor': ('name1', 'name2', 'name3'), \
    'comedy': ('name1', 'name2' , 'name4'), 'detective': ('name1', 'name1')}, 2)
    [('name1', 3), ('name2', 2)]

    """
    films_with_keywords = [(film, sum(film in films for films in \
    film_keywords.values())) for film \
    in set(film for films in film_keywords.values() for film in films)]
    films_with_keywords.sort(key=lambda x: (-x[1], x[0]))
    result = films_with_keywords[:num_of_films] if num_of_films > 0 else []
    return result
