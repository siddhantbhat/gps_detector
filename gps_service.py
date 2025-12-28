import geocoder
import requests

def get_coordinates():
    g = geocoder.ip('me')
    if not g.ok or not g.latlng:
        return None
    return {
        "latitude": g.latlng[0],
        "longitude": g.latlng[1]
    }

def reverse_geocode(lat, lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": lon,
        "format": "json"
    }
    headers = {"User-Agent": "GPS-Detector"}

    response = requests.get(url, params=params, headers=headers, timeout=5)
    if response.status_code != 200:
        return "Unknown location"

    data = response.json()
    return data.get("display_name", "Unknown location")
