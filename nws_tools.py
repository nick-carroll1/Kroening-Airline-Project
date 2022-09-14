# write a function that queries the National Weather Service for active alerts and returns a JSON object
# print the total number of alerts

import requests
import json


def get_alerts():
    url = "https://api.weather.gov/alerts/active"
    response = requests.get(url)
    return response.json()


def main():
    alerts = get_alerts()
    print("Total number of alerts: {}".format(len(alerts["features"])))
