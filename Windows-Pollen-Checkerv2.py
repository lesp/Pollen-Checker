from geopy.geocoders import Nominatim
from pypollen import Pollen
from win10toast import ToastNotifier
toaster = ToastNotifier()
geolocator = Nominatim()
while True:
    location = geolocator.geocode("Blackpool")
    lat = location.latitude
    lon = location.longitude
    pollen_status = Pollen(lat, lon).pollencount
    toaster.show_toast("The pollen level at your location is ",pollen_status,duration=10)
    time.sleep(15)
