"""
pandas
"""
import pandas as pd

def read_data(path_to_file):
    """
    reads the file and returns a DataFrame object, without additional data processing
    """
    df = pd.read_csv(path_to_file)
    return df


def max_counties(df):
    """
    returns a string, the name of the state with the largest number of counties.
    """

    return df.groupby('STNAME').CTYNAME.agg([len]).idxmax()[0]


def max_difference(df):
    """
    returns the string - the name of the county that contains the largest 
    absolute change in population during 2010-2015. For example, if the 
    population of a county over a 6-year 
    period is 100, 120, 80, 105, 100, 130, then its largest change over that period 
    will be | 130-80 | = 50.
    """
    data = df[df["CTYNAME"] != df["STNAME"]]
    i = (data[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013',\
'POPESTIMATE2014', 'POPESTIMATE2015']].max(axis = 1) - data[['POPESTIMATE2010', 'POPESTIMATE2011', \
'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']].min(axis=1)).idxmax()

    return data["CTYNAME"][i]


def conditional_counties(df):
    """
    In this file, the data is divided into four regions using 
    the "REGION" column. Create a function that finds counties 
    belonging to regions 1 or 2 whose name begins with 'Washington' 
    and POPESTIMATE2015 exceeded POPESTIMATE2014. This function should 
    return a 5x2 DataFrame with columns = ['STNAME', 'CTYNAME']
    """
    df1 = df[(df["REGION"] == 1) | (df["REGION"] == 2)]
    df1 = df1[df1["CTYNAME"].str.startswith("Washington")]
    df1 = df1[df1["POPESTIMATE2015"] > df1["POPESTIMATE2014"]]
    df1 = df1.iloc[:, [5,6]]
    return df1

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
