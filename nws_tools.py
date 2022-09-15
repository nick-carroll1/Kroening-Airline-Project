# write a function that queries the National Weather Service for active alerts and returns a JSON object
# convert the json object to a pandas dataframe
# print the response from the National Weather Service
# print the dataframe

import requests
import json
import pandas as pd


def get_alerts():
    url = "https://api.weather.gov/alerts/active"
    response = requests.get(url)
    return response.json()


def main():
    alerts = get_alerts()
    print("Total number of alerts: {}".format(len(alerts["features"])))
    df = pd.DataFrame(alerts["features"])
    print(df)
    # for alert in alerts["features"]:
    #   print(alert["properties"]["event"])


if __name__ == "__main__":
    main()
