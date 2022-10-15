import os
import requests
import config

BASE_URL="https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/"
LATITUDE=47.645523
LONGITUDE=-122.1339059
ZOOM=18
MAP_SIZE="500,500"
MAP_LAYER="Basemap,Buildings"
KEY=config.bing_maps_key

print(f"{BASE_URL}{LATITUDE},{LONGITUDE}/{ZOOM}?mapSize={MAP_SIZE}&mapLayer={MAP_LAYER}&key={KEY}")
response = requests.get(f"{BASE_URL}{LATITUDE},{LONGITUDE}/{ZOOM}?mapSize={MAP_SIZE}&mapLayer={MAP_LAYER}&key={KEY}")

with open('map.jpg', 'wb+') as f:
    f.write(response.content)
    f.close()

def get_bing_map_as_jpg(latitude, longitude, zoom, map_size):
    print(f"{BASE_URL}{latitude},{longitude}/{zoom}?mapSize={map_size}&mapLayer={MAP_LAYER}&key={KEY}")
    response = requests.get(f"{BASE_URL}{latitude},{longitude}/{zoom}?mapSize={map_size}&mapLayer={MAP_LAYER}&key={KEY}")
    
    with open('map.jpg', 'wb+') as f:
        f.write(response.content)

