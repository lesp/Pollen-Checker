import requests
import json
import os
from pypollen import Pollen
import notify2
#Images
cwd = os.getcwd()
VeryHigh = cwd+"/Images/VeryHighPollen.png"
High = cwd+"/Images/HighPollen.png"
Moderate = cwd+"/Images/ModeratePollen.png"
Low = cwd+"/Images/LowPollen.png"
print(VeryHigh)
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']
pollen_status = Pollen(lat, lon).pollencount
pollen_status = "Low"
print(pollen_status)
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
