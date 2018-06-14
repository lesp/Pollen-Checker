import requests
import json
import os
from pypollen import Pollen
import notify2
import time
#Images
cwd = os.getcwd()
VeryHigh = cwd+"/Images/VeryHighPollen.png"
High = cwd+"/Images/HighPollen.png"
Moderate = cwd+"/Images/ModeratePollen.png"
Low = cwd+"/Images/LowPollen.png"
while True:
    send_url = 'http://ipinfo.io/json'
    
    location = json.loads(r.text)
    location = location["loc"]
    location = location.split(",")
    lat = location[0]
    lon = location[1]
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
    if pollen_status == "Low":
        n = notify2.Notification("The pollen level at your location is ",pollen_status,icon=Low)
        n.show()
    time.sleep(15)