import pandas as pd

def read_data(path_to_file):
    """
    Reads the file and returns a DataFrame object without additional data processing.
    """
    df = pd.read_csv(path_to_file)
    return df


def max_counties(df):
    """
    Returns the name of the state with the largest number of counties as a string.
    """
    return df.groupby('STNAME').CTYNAME.agg([len]).idxmax()[0]


def max_difference(df):
    """
    Returns the name of the county with the largest absolute change in population during 2010-2015.
    """
    data = df[df["CTYNAME"] != df["STNAME"]]
    population_change = data[['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013',
                              'POPESTIMATE2014', 'POPESTIMATE2015']]
    max_change_index = (population_change.max(axis=1) - population_change.min(axis=1)).idxmax()
    return data["CTYNAME"][max_change_index]


def conditional_counties(df):
    """
    Finds counties belonging to regions 1 or 2 whose name begins with 'Washington' and POPESTIMATE2015 
    exceeded POPESTIMATE2014. Returns a DataFrame with columns = ['STNAME', 'CTYNAME'].
    """
    df_filtered = df[(df["REGION"].isin([1, 2])) & (df["CTYNAME"].str.startswith("Washington")) &
                     (df["POPESTIMATE2015"] > df["POPESTIMATE2014"])]
    return df_filtered[['STNAME', 'CTYNAME']]

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
