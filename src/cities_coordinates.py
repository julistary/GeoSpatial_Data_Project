import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster

def sf_coordinates(): 
    """
    Gives the coordinates of San Francisco
    Returns:
        The coordinates as a point
    """
    return {'type': 'Point', 'coordinates': [37.773972, -122.431297]}

def london_coordinates():
    """
    Gives the coordinates of London
    Returns:
        The coordinates as a point
    """
    return {'type': 'Point', 'coordinates': [51.509865, -0.118092]}

def ny_coordinates():
    """
    Gives the coordinates of New York
    Returns:
        The coordinates as a point
    """
    return {'type': 'Point', 'coordinates': [40.730610, -73.935242]}

def map_city(city):
    """
    Creates a map of the city
    Args: 
    city (point): the coordinates of the city to be plotted
    Returns:
        The map of the city
    """
    return Map(location=city['coordinates'],zoom_start=15)

