"""
Module: counties_process

This module contains functions to process census data for counties.
"""

import pandas as pd

def read_data(path_to_file):
    """
    Reads the file and returns a DataFrame object, without additional data processing

    Parameters:
    path_to_file (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame object containing the data.
    """
    df = pd.read_csv(path_to_file)
    return df

def max_counties(df):
    """
    Returns the name of the state with the largest number of counties.
    """
    return df['STNAME'].value_counts().idxmax()

def max_difference(df):
    """
    Returns the name of the county with the largest absolute change in population during 2010-2015.
    """
    data = df[df["CTYNAME"] != df["STNAME"]]
    pop_columns = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 
                   'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
    max_pop = data[pop_columns].max(axis=1)
    min_pop = data[pop_columns].min(axis=1)
    max_change_idx = (max_pop - min_pop).idxmax()
    return data.loc[max_change_idx, 'CTYNAME']

def conditional_counties(df):
    """
    Finds counties belonging to regions 1 or 2 whose name begins with 'Washington' and 
    POPESTIMATE2015 exceeded POPESTIMATE2014.
    """
    washington_counties = df[(df["REGION"].isin([1, 2])) & 
                              (df["CTYNAME"].str.startswith("Washington")) & 
                              (df["POPESTIMATE2015"] > df["POPESTIMATE2014"])]
    result = washington_counties[['STNAME', 'CTYNAME']].head(5)
    return result

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
