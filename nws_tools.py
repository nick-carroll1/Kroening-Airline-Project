# write a tool that gets all active alerts from the NWS
# return a JSON and print the number of active alerts

import os
import requests
import json
import pandas as pd


def get_alerts():
    # define the URL for the NWS API
    url = "https://api.weather.gov/alerts/active"
    # send the request to the NWS API
    response = requests.get(url)
    # return the response from the NWS API
    return response.json()


def response_transform():
    # get the JSON object from the NWS API
    json_object = get_alerts()
    # keep the severity, certainty, and last two characters of the senderName as a pandas dataframe
    df = pd.DataFrame(
        [
            [
                x["properties"]["severity"],
                x["properties"]["certainty"],
                x["properties"]["senderName"][-2:],
            ]
            for x in json_object["features"]
        ],
        columns=["severity", "certainty", "senderName"],
    )
    # print the number of active alerts from senderName "WS"
    print({"National-Level Alerts: ": len(df[df["senderName"] == "WS"])})
    # drop rows where the senderName is "WS"
    df = df[df["senderName"] != "WS"]
    # add an index column with new index values
    df = df.reset_index(drop=True)
    # add an column called index with the index values
    df["index"] = df.index
    # print the number of active alerts after dropping rows where the senderName is "WS"
    print({"Alerts after removing National-Level Alerts: ": len(df)})
    # convert the dataframe to a JSON object
    json_object = df.to_json(orient="records")
    # return the JSON object
    return json_object


if __name__ == "__main__":
    response_transform()
