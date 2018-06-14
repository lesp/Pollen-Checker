import requests
import json
import time
from pypollen import Pollen
from blinkt import set_pixel, set_brightness, show, clear
set_brightness(0.1)
while True:
    send_url = "http://ipinfo.io/json"
    r = requests.get(send_url)
    location = json.loads(r.text)
    location = location["loc"]
    location = location.split(",")
    lat = location[0]
    lon = location[1]
    pollen_status = Pollen(lat, lon).pollencount
    pollen_status = "Moderate"
    if pollen_status == "Very High":
        clear()
        for i in range(8):
            set_pixel(i,255,0,0)
            show()
    elif pollen_status == "High":
        clear()
        for i in range(8):
            set_pixel(i,255,153,51)
            show()
    elif pollen_status == "Moderate":
        clear()
        for i in range(8):
            set_pixel(i,250,250,102)
            show()
    elif pollen_status == "Low":
        clear()
        for i in range(8):
            set_pixel(i,0,255,0)
            show()
    time.sleep(15)
