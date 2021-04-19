import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd

def institution(df,city,map):
    """
    Places the given data of a dataframe on the map
    Args:
        df (dataframe): the dataframe from which the data to be located is taken 
        city (string): the city where you want to place the data (used to filter the dataframe)
        map (folium.Map): the map where the data has to be placed.
    Returns:
        The map with the data placed
    """

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


def final_location(coordinates_,map_lnd):
    """
    Places the final location on the map
    Args:
        coordinates_ (list): coordinates of the final location
        map_lnd (folium.Map): the map where the data has to be placed.
    """

    icono = Icon(color = "white",
             prefix = "fa",
             icon = "trophy",
             icon_color = "black")

    loc = {"location": coordinates_,
      "tooltip": "Gaming Company"}
    
    marker_company = Marker(**loc, icon = icono)
    marker_company.add_to(map_lnd)

def nearby(df_places,map_lnd):
    """
    Places what is near the final location on the map
    Args:
        df_places(df): the dataframe with the coordinates information
        map_lnd (folium.Map): the map where the data has to be placed.
    """

    for i, row in df_places.iterrows():
        p = {
            "location": row["coordinates"],
            "tooltip" : row["name"]
            }
        if row['place'] == 'starbucks':
            icon = Icon(color = "green",
                        prefix = "fa",
                        icon = "coffee",
                        icon_color = "black"
            )
        elif row['place'] == 'school':

            icon = Icon(color = "red",
                        prefix = "fa",
                        icon = "book",
                        icon_color = "black"
            )
        elif row['place'] == 'party':
            icon = Icon(color = "pink",
                        prefix = "fa",
                        icon = "glass",
                        icon_color = "black"
            )
        elif row['place'] == 'vegan':
            icon = Icon(color = "blue",
                        prefix = "fa",
                        icon = "cutlery",
                        icon_color = "black"
            )
        else:
            icon = Icon(color = "orange",
                        prefix = "fa",
                        icon = "futbol-o",
                        icon_color = "black"
            )
        Marker(**p,icon = icon ).add_to(map_lnd)