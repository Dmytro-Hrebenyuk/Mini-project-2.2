"""
counties_process.py
Module for processing county data.
"""

import pandas as pd

def read_data(path_to_file):
    """
    Read the file and return a DataFrame object, without additional data processing.

    Args:
        path_to_file (str): Path to the file.

    Returns:
        pandas.DataFrame: DataFrame containing the data.
    """
    df = pd.read_csv(path_to_file)
    return df

def max_counties(df):
    """
    Return the name of the state with the largest number of counties.

    Args:
        df (pandas.DataFrame): DataFrame containing county data.

    Returns:
        str: Name of the state with the largest number of counties.
    """
    return df['STNAME'].value_counts().idxmax()

def max_difference(df):
    """
    Return the name of the county with the largest absolute change in population during 2010-2015.

    Args:
        df (pandas.DataFrame): DataFrame containing county data.

    Returns:
        str: Name of the county with the largest absolute population change.
    """
    data = df[df["CTYNAME"] != df["STNAME"]]
    pop_columns = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
    max_pop = data[pop_columns].max(axis=1)
    min_pop = data[pop_columns].min(axis=1)
    max_change_idx = (max_pop - min_pop).idxmax()
    return data.at[max_change_idx, 'CTYNAME']

def conditional_counties(df):
    """
    Find counties belonging to regions 1 or 2 whose name begins with 'Washington' 
    and POPESTIMATE2015 exceeded POPESTIMATE2014.

    Args:
        df (pandas.DataFrame): DataFrame containing county data.

    Returns:
        pandas.DataFrame: DataFrame with columns ['STNAME', 'CTYNAME'].
    """
    condition = (df['REGION'].isin([1, 2])) & (df['CTYNAME'].str.startswith("Washington")) & (df['POPESTIMATE2015'] > df['POPESTIMATE2014'])
    filtered_df = df[condition][['STNAME', 'CTYNAME']].head()
    return filtered_df

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
