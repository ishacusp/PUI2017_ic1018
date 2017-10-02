from __future__ import print_function
import sys
import json
import csv

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
    
##To check if the number of arguments are 4 or not    
if not len(sys.argv)==4:
    print("Incorrect number of arguments. Enter the arguments as python file <python_file.py> <MTA Key> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()    
    
key=sys.argv[1]
bus_line=sys.argv[2]
file_csv=sys.argv[3]

##This url connects MTA API server to the file
url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+ bus_line
#print (url)

##loading the json file in data
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

##counting the number of buses which are active
count_active_buses=len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

##opening the input csv file, extracting the contents of JSON file stored as 'data' and rendering that data into the input csv file
with open(file_csv, 'w') as file_input:
    writer=csv.writer(file_input)
    writer.writerow(['Latitude','Longitude','Stop Name','Stop Status'])
    for i in range(count_active_buses):
        location = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
        if data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']=={}:
            stop='N/A'
            status='N/A'
        else:
            
            stop=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            
            status=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        
        writer=csv.writer(file_input)
##writing the location, stop name and stop status in the csv file
        writer.writerow([location['Latitude'],location['Longitude'],stop,status]) 