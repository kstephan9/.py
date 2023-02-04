from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap

geolocator = Nominatim()
location = ''
location = geolocator.geocode("1750-5 West Citracado Pkwy, Escondido, CA")
#location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

pp.figure(figsize=(10,5))
#https://matplotlib.org/basemap/users/examples.html

