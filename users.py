from geocodio import GeocodioClient

#import pygeocodio
#from pygeocodio import GeocodioClient

import my_secrets
from my_secrets import GeocodioAPIKey

client = GeocodioClient(GeocodioAPIKey)

def test_bit(x,n): 
    """
    tests if the nth bit of x is set 
    """
    if (x & (1<<n)):
        return 1 
    return 0 

def set_bit(num, index):
    mask = 1 << index
    num |= mask 
    return num 

class Student: 
    def __init__(self, ID, First, Last, Address, Travel, Session): 
        self.ID = ID
        self.FirstName = First 
        self.LastName = Last
        self.Address = Address
        self.Geocoded = client.geocode(Address)
        self.Lat = Geocoded.coords[1]
        self.Long = Geocoded.coords[0]
        self.TravelMethod = Travel 
        self.Session = Session
        self.Distances = []
        self.Schedule = '' 
    
    def get_name(self): 
        return First + ' ' + Last
    
    def OSRM_get_distance_to(self, teacher, osrm_server_url):
        t_lat = teacher.Lat 
        t_long = teacher.Long 
        t_longlat = str(t_long)+','+str(t_lat)+';'
        s_longlat = str(s_long)+','+str(s_lat)+'?'
        request_url = f'https://{osrm_server_url}route/v1/driving/'
        request_url += (t_longlat+s_longlat+'?')
        response = requests.get(request_url) 
        jsonified = json.loads(response.text)
        distance = jsonified["routes"][0]["duration"]
        return distance
    
    def OX_get_distance_to(self, teacher):
        pass

    def get_directions_to(self, teacher, osrm_server_url): 
        pass
    
    def get_distances_to(self, teachers): 
        for teacher in teachers: 
            self.Distances.append(OX_get_distance_to(teacher))

    def get_scheduled_teacher(self, schedule): 
        my_session = self.Session 
        ssn = schedule.my_session 
        for scheduled_teacher in ssn: 
            for student in scheduled_teacher: 
                if student == self.ID: 
                    self.Schedule = scheduled_teacher 

class Teacher: 
    def __init__(self, ID, First, Last, Clinic, Address, Availability):
        self.ID = ID
        self.FirstName = First 
        self.LastName = Last 
        self.ClinicName = Clinic 
        self.ClinicAddress = Address
        self.Geocoded = client.geocode(Address)
        self.Lat = Geocoded.coords[1]
        self.Long = Geocoded.coords[0]
        self.AvailabilityData = Availability
        self.Availability = 100000000001
        self.Schedule = '' 
    
    def get_schedule(self, schedule): 
        pass 
    
    def set_availability(self): 
        for data in self.AvailabilityData: 
            pass
            
    def print_teacher(self):
        print(self.ID, self.FirstName, self.Lat, self.Long)
