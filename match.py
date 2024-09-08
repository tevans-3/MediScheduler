import osmnx as ox 
import networkx as nx
import nominatim
import csv
import geopandas as gpd 
import matplotlib.pyplot as plt
import shapely
from shapely.geometry import Point, LineString, Polygon
from pyproj import CRS 
from pathlib import Path

import users
from users import Student, Teacher

import schedule 
import map

def transit_users_first(students, teachers): 
    """
    """
    transit_users = [student for student in students if student.travel == 'Public Transit']
    