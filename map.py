import OSMPythonTools 
from OSMPythonTools import Overpass 

import osmnx as ox 
import networkx as nx
import nominatim

class Map: 
    def __init__(self, city): 
        self.city = city 
        self.vis_graph = ox.graph_from_place(city, network_type ='all_public')
        self.area_id = nominatim.query(city).areaId()

class PublicTransit(Map): 
    def __init__(self): 
        super(PublicTransit, self).__init__(city)
        self.all_stops = {}
        self.query()
    
    def query(self): 
        query_result = overpass.query('relation'['highway'='bus_stop'], 'way'['railway'='tram_stop'])
        for result in query_result['elements']: 
            all_stops[query_result["tags"]["name"]] = (query_result["lon"], query_result["lat"]) 

class Driving(Map): 
    def __init__(self): 
        super(Driving, self).__init__(city)
        self.all_roads = {}
        self.query()
    
    def query(self): 
        query_result = overpass.query('relation'['highway'])
        for result in query_result['elements']: 
            all_roads[query_result["tags"]["name"]] = (query_result["lon"], query_result["lat"]) 
