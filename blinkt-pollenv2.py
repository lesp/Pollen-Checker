import time
from pypollen import Pollen
from blinkt import set_pixel, set_brightness, show, clear
from geopy.geocoders import Nominatim
geolocator = Nominatim()
set_brightness(0.1)
while True:
    location = geolocator.geocode("Blackpool")
    lat = location.latitude
    lon = location.longitude
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
