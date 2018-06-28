import os
from pypollen import Pollen
import time
from geopy.geocoders import Nominatim
from gtts import gTTS
geolocator = Nominatim()
#Images
cwd = os.getcwd()
while True:
    location = geolocator.geocode("Blackpool")
    lat = location.latitude
    lon = location.longitude
    pollen_status = Pollen(lat, lon).pollencount
    text = "The pollen level at your location is "+pollen_status
    speech = (gTTS(text=text))
    speech.save(cwd+"/speech.mp3")
    speech_path = "cmdmp3.exe "+cwd+"/speech.mp3"
    os.system(speech_path)
    time.sleep(15)
