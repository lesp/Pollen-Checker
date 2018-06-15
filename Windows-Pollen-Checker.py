import requests
import json
from pypollen import Pollen
from win10toast import ToastNotifier
toaster = ToastNotifier()
while True:
    send_url = "http://ipinfo.io/json"
    r = requests.get(send_url)
    location = json.loads(r.text)
    location = location["loc"]
    location = location.split(",")
    lat = location[0]
    lon = location[1]
    pollen_status = Pollen(lat, lon).pollencount
    toaster.show_toast("The pollen level at your location is ",pollen_status,duration=10)
    time.sleep(15)
