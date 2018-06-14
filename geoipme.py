import requests
import json
import os
from pypollen import Pollen
import notify2
#Images
cwd = os.getcwd()
VeryHigh = cwd+"/Images/HighPollen.png"
print(VeryHigh)
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']
pollen_status = Pollen(lat, lon).pollencount
notify2.init("Pollen Count Data")
if pollen_status == "Very High":
    n = notify2.Notification("The pollen level at your location is ",pollen_status,icon=VeryHigh)
    n.show()
