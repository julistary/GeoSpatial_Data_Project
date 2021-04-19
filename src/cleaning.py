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

    
def kepler_cleaning(df_places,df_final):
    """
    Prepares and concatenates the dataframes so that it can be plotted on a Kepler
    Args:
        df_places(df): dataframe that will be plotted
        df_final(df):  dataframe that will also be plotted
    Returns:
        The new dataframe cleaned
    """
    df_places.drop(['_id'], axis = 1, inplace = True)

    df_places.head()

    list(df_final.geometry)[0]

    df_final.head()
    new_row = {'name':'Gaming Company', 'location': list(df_final.geometry)[0], 'place' : 'company', 'coordinates' : [list(df_final.geometry)[0]['coordinates'][1], list(df_final.geometry)[0]['coordinates'][0]]}
    df_places = df_places.append(new_row, ignore_index=True)

    df_places.tail()

    latit = []
    longit = []
    for coord in list(df_places['coordinates']):
        latit.append(coord[0])
        longit.append(coord[1])

    df_places['latitude'] = latit
    df_places['longitude'] = longit

    return df_places