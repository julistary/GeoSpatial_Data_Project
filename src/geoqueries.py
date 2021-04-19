import pandas as pd
import requests
import json
from pymongo import MongoClient
import geopandas
conn = MongoClient("localhost:27017")
db = conn.get_database("ironhack")
from pymongo import GEOSPHERE

collection = db.get_collection("preferences")

def grades(x):
    """
    Transforms a grade into a score from 1 to 4 
    Args:
        x(int): the grade
    Returns:
        The score as an integer
    """
    if x == 0:
        return 0
    elif (x > 0) and (x <= 8):
        return 1
    elif (x > 8) and (x <= 20):
        return 2
    else:
        return 3


def places_counts(coordinates,df):
    """
    Creates a dataframe with the result of the geoqueries
    Args:
        df (df): the dataframe where the columns will be added
        coordinates (list): the coordinates to be iterated over
    Returns:
        The new dataframe
    """
    party_counts = []
    starbucks_counts = []
    school_counts = []
    vegan_counts = []
    basket_counts = []
    for c in coordinates:
        query = {"location": {"$near": {"$geometry": c, "$maxDistance": 2000}}}
        list_ = list(collection.find(query))
        party = 0
        starbucks = 0
        school = 0
        vegan = 0
        basket = 0
        for l in list_:
            if l['place'] == 'party':
                party += 1
            elif l['place'] == 'starbucks':
                starbucks += 1
            elif l['place'] == 'school':
                school += 1
            elif l['place'] == 'vegan':
                vegan += 1
            elif l['place'] == 'basket':
                basket += 1
        party_counts.append(party)
        starbucks_counts.append(starbucks)
        school_counts.append(school)
        vegan_counts.append(vegan)
        basket_counts.append(basket)

    df['party'] = party_counts
    df['starbucks'] = starbucks_counts
    df['school'] = school_counts
    df['vegan'] = vegan_counts
    df['basket'] = basket_counts

    return df

def best_option(df):
     """
    Creates a dataframe with the best option
    Args:
        df (df): the dataframe where the information is stored
    Returns:
        The new dataframe
    """
    df.weighted_result.max()

    df_ = [df['weighted_result'] == df.weighted_result.max()]

    is_max = df.loc[:, "weighted_result"] == df.weighted_result.max()
    df_final = df.loc[is_max]
    return df_final

def near_option(df_final):
    """
    Creates a dataframe with all the places near the best option
    Args:
        df_final (df): the dataframe where the information of the best option is stored
    Returns:
        The new dataframe
    """
    party_coord = []
    starbucks_coord = []
    school_coord = []
    vegan_coord = []
    basket_coord = []

    query = {"location": {"$near": {"$geometry": list(df_final['geometry'])[0], "$maxDistance": 2000}}}
    query

    df_places = pd.DataFrame(list(collection.find(query)))

    coordinates = []
    for point in list(df_places['location']):
        coordinates.append([point['coordinates'][1],point['coordinates'][0]])
    df_places['coordinates'] = coordinates

    return df_places

