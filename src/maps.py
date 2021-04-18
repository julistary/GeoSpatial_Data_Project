import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd

def institution(df,city,map):

    for i, row in df[df.city == city].dropna().iterrows():
        company = {
            "location":[row["latitude"], row["longitude"]],
            "tooltip" : row["company"]
        }
        
        icon = Icon(color = "green",
                    prefix = "fa",
                    icon = "institution",
                    icon_color = "black"
        )
            
        Marker(**company,icon = icon ).add_to(map)
    return(map)

