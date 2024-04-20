"""
counties_process.py

This module provides functions to process county data.

"""

import pandas as pd

def read_data(path_to_file):
    """
    Reads the file and returns a DataFrame object without additional data processing.
    
    Parameters:
    path_to_file (str): Path to the CSV file.
    
    Returns:
    pandas.DataFrame: DataFrame object containing the data from the CSV file.
    """
    return pd.read_csv(path_to_file)


def max_counties(df):
    """
    Returns the name of the state with the largest number of counties.

    Parameters:
    df (pandas.DataFrame): DataFrame object containing the data.

    Returns:
    str: Name of the state with the largest number of counties.
    """
    return df['STNAME'].value_counts().idxmax()


def max_difference(df):
    """
    Returns the name of the county with the largest absolute change in population during 2010-2015.

    Parameters:
    df (pandas.DataFrame): DataFrame object containing the data.

    Returns:
    str: Name of the county with the largest absolute change in population.
    """
    data = df[df['CTYNAME'] != df['STNAME']]
    pop_columns = [f'POPESTIMATE{i}' for i in range(2010, 2016)]
    differences = data[pop_columns].max(axis=1) - data[pop_columns].min(axis=1)
    return data.loc[differences.idxmax(), 'CTYNAME']


def conditional_counties(df):
    """
    Finds counties belonging to regions 1 or 2 whose name begins with 'Washington' 
    and POPESTIMATE2015 exceeded POPESTIMATE2014.

    Parameters:
    df (pandas.DataFrame): DataFrame object containing the data.

    Returns:
    pandas.DataFrame: DataFrame with columns ['STNAME', 'CTYNAME'].
    """
    condition = (df['REGION'].isin([1, 2])) & \
                (df['CTYNAME'].str.startswith("Washington")) & \
                (df['POPESTIMATE2015'] > df['POPESTIMATE2014'])
    return df.loc[condition, ['STNAME', 'CTYNAME']]


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
