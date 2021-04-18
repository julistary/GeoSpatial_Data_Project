import pandas as pd
import requests
import json
from pymongo import MongoClient
import geopandas
conn = MongoClient("localhost:27017")
db = conn.get_database("ironhack")
from pymongo import GEOSPHERE

def grades(x):
    if x == 0:
        return 0
    elif (x > 0) and (x <= 8):
        return 1
    elif (x > 8) and (x <= 20):
        return 2
    else:
        return 3
