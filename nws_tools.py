# write a tool that gets all active alerts from the NWS
# return a JSON and print the number of active alerts

import requests
import pandas as pd


def get_alerts():
    # define the URL for the NWS API
    url = "https://api.weather.gov/alerts/active"
    # send the request to the NWS API
    response = requests.get(url, timeout=5)
    # return the response from the NWS API
    return response.json()


def package_alerts():
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
    # drop rows where the senderName is "WS"
    df = df[df["senderName"] != "WS"]
    # add an index column with new index values
    df = df.reset_index(drop=True)
    # add an column called index with the index values
    df["index"] = df.index
    # convert the dataframe to a JSON object
    json_object = df.to_json(orient="records")
    # return the JSON object
    return json_object


def alert_info():
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
    # print the total number of alerts
    print("Total number of alerts: ", len(df))
    # print the number of active alerts from senderName "WS"
    print("National-Level Alerts: ", len(df[df["senderName"] == "WS"]))
    # print the number of active alerts after dropping rows where the senderName is "WS"
    print("State-Level Alerts: ", len(df[df["senderName"] != "WS"]))
    # print number of extreme alerts
    print("Extreme Alerts: ", len(df[df["severity"] == "Extreme"]))
    # print the five states with the most active alerts
    print(
        "States with the most active alerts: \n",
        df["senderName"].value_counts().head(),
    )
