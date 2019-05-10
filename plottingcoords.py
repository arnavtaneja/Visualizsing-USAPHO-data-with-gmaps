# import gmplot package
import gmplot
from geopy.geocoders import Nominatim
from physicsoly import city 
from physicsoly import state
from physicsoly import school

gmap3 = gmplot.GoogleMapPlotter(37.6872,-97.3301, 5)

geolocator = Nominatim(user_agent="enterkeyhere")

latitude_list = []
longitude_list = []

#max = len(state)
max = len(state)

for r in range(0,max ):
	locationstring =city[r] + " " + state[r]
	location = geolocator.geocode(locationstring)
	latitude_list.append(location.latitude)
	longitude_list.append(location.longitude)
	print(locationstring)
	print(location.latitude, location.longitude)






# scatter method of map object 
# scatter points on the google map
gmap3.scatter( latitude_list, longitude_list, '#aa00ff', size = 20000, marker = False )

# Plot method Draw a line in
# between given coordinates


			#gmap3.plot(latitude_list, longitude_list, 'cornflowerblue', edge_width = 2.5)



gmap3.draw( "/path/map.html" )