import requests

def get_geolocation(ip):
    # Example using ipinfo.io
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        loc = data.get("loc", None)  # loc returns "latitude,longitude"
        if loc:
            lat, lon = map(float, loc.split(","))
            return lat, lon
    return None, None

