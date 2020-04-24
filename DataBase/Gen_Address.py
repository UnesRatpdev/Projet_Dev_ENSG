import random
import socket
import urllib
import json
from itertools import count


from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

class Gen_Address:
    def __init__(self):
        print("Created")

    def Gen_Address(self):
        try:
            geolocator = Nominatim(user_agent="Projet_Dev")
            long = random.uniform(42, 51)
            long = round(long, 10)

            lat = random.uniform(2, 8)
            lat = round(lat, 10)

            loc = "" + str(long) + "," + str(lat)
            location = geolocator.reverse(loc)
            country_string = json.dumps(location.raw, ensure_ascii=True)
            country = json.loads(country_string)
            return location
        except (GeocoderTimedOut,AttributeError,KeyError):
            return Gen_Address()

    def Check_Address_in_Fr(self,Gen_Address):
        try:
            location = Gen_Address
            country_string = json.dumps(location.raw, ensure_ascii=True)
            if (country_string != {"error": "Unable to geocode"}):
                country = json.loads(country_string)
                if (country["address"]["country"] == "France"):
                    return True
            return False
        except (AttributeError,KeyError):
            return False

    def Gen_Address_local(self):
        lat = random.uniform(42, 51)
        lat = round(lat, 10)

        long = random.uniform(2, 8)
        long = round(long, 10)
        return [long,lat]

    def Gen_Address_Within_Distane(self,lat0,long0):
        #0.03 degres = 3. km
        long = random.uniform(long0-0.03,long0+0.03)
        long = round(long, 10)

        lat = random.uniform(lat0-0.03, lat0+0.03)
        lat = round(lat, 10)
        return [long, lat]








