import requests
import json

import polyline
import matplotlib.pyplot as plt
import pandas as pd

import strava_data as strava

def get_elevation(lat, long):
    query = ('https://api.open-elevation.com/api/v1/lookup'
             f'?locations={lat},{long}')
    r = requests.get(query).json()  
    item = r["results"][0]
    return item["elevation"]

def get_elevations(coords):
    strs = [f"{x},{y}" for x,y in coords]
    strs = "|".join(strs)
    query = ('https://api.open-elevation.com/api/v1/lookup'
             f'?locations={strs}')
    r = requests.get(query).json()  
    rs = r["results"]
    elevs = [r["elevation"] for r in rs]
    return elevs

def activity_effort_score(item, weights):
    distance_score = item["distance"]*weights["distance"]
    moving_time_score = item["moving_time"]*weights["moving_time"]
    average_speed_score = item["average_speed"]*weights["average_speed"]
    max_speed_score = item["max_speed"]*weights["max_speed"]

    if "elev_low" in item.keys():
        elev_low = item["elev_low"]
        elev_high = item["elev_high"]
        elev_diff_score = (elev_high - elev_low)*weights["elevation_diff"]
    else:
        elev_low, elev_high, elev_diff_score = 0, 0, 0
    #encoded_coords = item["map"]
    #coords = polyline.decode(encoded_coords)
    #elevs = get_elevations(coords)
    score  = distance_score + moving_time_score + average_speed_score + \
    max_speed_score + elev_diff_score
    return score


def process(weights):
    data = strava.process()
    for d in data:
        score = activity_effort_score(d, weights)
        d["score"] = score
    return data


WEIGHTS = {
    "distance": 0.7,
    "moving_time": 0.15,
    "average_speed": 0.15,
    "max_speed": 0,
    "elevation_diff": 0,
}

if __name__ == "__main__":
    scores = process(WEIGHTS)
    print(scores)



