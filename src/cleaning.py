import pandas as pd

def preliminary_cleaning(df): 
    """
    Cleans a dataframe.
    Args:
        df (df): the dataframe that wants to be cleaned
    Returns:
        The dataframe cleaned
    """
    df = df.dropna()
    df.reset_index(drop=True,inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def column_point(df):
    """
    Creates a new column to add to the dataframe with the coordinates as a point
    Args:
        df (df): the dataframe where the new column will be created 
    Returns:
        The new column
    """
    lat = list(df.latitude)
    long = list(df.longitude)
    coordinates = []
    for lt,lg in zip(lat,long):
        coord = [lg,lt]
        coordinates.append({"type": "Point",  "coordinates": coord})
    return coordinates

    