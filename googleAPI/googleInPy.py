import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDJxtj9236MbEc16B_D8zDpSIBxXAhmR54')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

#given a place - find the location(lat and long) and place_id
map_result = gmaps.find_place('VT', 'textquery',
                                fields=['geometry/location', 'place_id'],
                                location_bias='point:90,90', language = 'en-AU')

latitude  = map_result.get('candidates')[0].get('geometry').get('location').get('lat')
longitude  = map_result.get('candidates')[0].get('geometry').get('location').get('lng')
print ("lat:",latitude);
print ('long:', longitude);