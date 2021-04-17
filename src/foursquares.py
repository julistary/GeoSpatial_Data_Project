import requests
import json
from dotenv import load_dotenv
import os
import pandas as pd
import src.foursquares as fs
load_dotenv()

tok1= os.getenv("tok1")
tok2= os.getenv("tok2")

url_query = 'https://api.foursquare.com/v2/venues/explore'

def f_call(city,query):
    params = {
        "client_id": tok1,
        "client_secret": tok2,
        "v": "20180323",
        "ll": f"{city.get('coordinates')[0]},{city.get('coordinates')[1]}",
        "query": query, 
        "limit": 100    
    }
    return requests.get(url= url_query, params = params).json()

def call_to_df(list_):
    lista_ = []
    data = list_.get("response").get("groups")[0].get("items")
    name = []
    latitude = []
    longitude = []
    for d in data:
        paralista = {}
        paralista["name"] = d.get("venue").get("name")
        paralista["latitude"] = d.get("venue").get("location").get("lat")
        paralista["longitude"] = d.get("venue").get("location").get("lng")
        lista_.append(paralista)
                                               
    documentos = []
    for diccionario in lista_:
        temporal = {
            "name": diccionario.get("name"),
            "location": {"type": "Point", "coordinates": [diccionario.get("latitude"), diccionario.get("longitude")]}

        }
        documentos.append(temporal)


    df = pd.DataFrame(documentos)
    df.head()
    return df



