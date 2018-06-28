import os
from pypollen import Pollen
import notify2
import time
from geopy.geocoders import Nominatim
geolocator = Nominatim()
#Images
cwd = os.getcwd()
VeryHigh = cwd+"/Images/VeryHighPollen.png"
High = cwd+"/Images/HighPollen.png"
Moderate = cwd+"/Images/ModeratePollen.png"
Low = cwd+"/Images/LowPollen.png"
while True:
    location = geolocator.geocode("Blackpool")
    lat = location.latitude
    lon = location.longitude
    pollen_status = Pollen(lat, lon).pollencount
    notify2.init("Pollen Count Data")
    if pollen_status == "Very High":
        n = notify2.Notification("The pollen level at your location is ",pollen_status,icon=VeryHigh)
        n.show()
    elif pollen_status == "High":
        n = notify2.Notification("The pollen level at your location is ",pollen_status,icon=High)
        n.show()
    elif pollen_status == "Moderate":
        n = notify2.Notification("The pollen level at your location is ",pollen_status,icon=Moderate)
        n.show()
    elif pollen_status == "Low":
        n = notify2.Notification("The pollen level at your location is ",pollen_status,icon=Low)
        n.show()
    time.sleep(15)
