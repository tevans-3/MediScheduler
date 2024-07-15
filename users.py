import geopy
from geopy.geocoders import Nominatim 
import requests

geolocator = Nominatim(user_agent="my_app")

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
        self.Lat = geolocator.geocode(Address).latitude
        self.Long = geolocator.geocode(Address).longitude
        self.TravelMethod = Travel 
        self.Session = Session
        self.Schedule = '' 
    
    def get_name(self): 
        return First + ' ' + Last
    
    def get_distance_to(self, teacher, osrm_server_url):
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
        self.Lat = geolocator.geocode(Address).latitude
        self.Long = geolocator.geocode(Address).longitude
        self.AvailabilityData = Availability
        self.Availability = 10000001
        self.Schedule = '' 
    
    def get_schedule(self, schedule): 
        pass 
    
    def set_availability(self): 
        pass 
        #for avail in self.AvailabilityData: 
        
    def print_teacher(self):
        print(self.ID, self.FirstName, self.Lat, self.Long)
