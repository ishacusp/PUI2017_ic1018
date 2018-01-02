from __future__ import print_function
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys

##checking if the number of arguments are equal to 3 or not
if not len(sys.argv)==3:
    print("Incorrect number of arguments. Enter the arguments as python file <python_file.py> <MTA Key> <BUS_LINE>")
    sys.exit()
    
key=sys.argv[1]
bus_line=sys.argv[2]

    
##Extracting the JSON file through MTA API server key
url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+ bus_line

##Loading the JSON file and storing it as pandas dataframe
lib=urllib.urlopen(url)
data=lib.read().decode('utf-8')
data=json.loads(data)

##number of active buses
count_active_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

##printing the number of active buses at the input bus line
print('Bus Line :',bus_line, '\nNumber of active buses:',count_active_buses)

##extracting the location coordinates of the active buses from 'data' and storing it to a variable 'location'
for i in range(count_active_buses):
    location=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
    ##printing the location coordinates of the buses
    print('Bus ',i,' is at latitude ',location['Latitude'],' and longitude ',location['Longitude'])
