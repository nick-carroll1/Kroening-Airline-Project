'''Module of functions to query the NWS database for active alerts'''

# write a tool that gets all active alerts from the NWS
# return a JSON and print the number of active alerts

import requests
import pandas as pd


def get_alerts():
    '''Return a JSON payload of all active alerts'''
    # define the URL for the NWS API
    url = "https://api.weather.gov/alerts/active"
    # send the request to the NWS API
    response = requests.get(url, timeout=5)
    # return the response from the NWS API
    return response.json()


def package_alerts():
    '''Transform the resulting JSON payload into an easier to manipulate version'''
    # get the JSON object from the NWS API
    json_object = get_alerts()
    # keep the severity, certainty, and last two characters of the senderName as a pandas dataframe
    alert_df = pd.DataFrame(
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
    alert_df = alert_df[alert_df["senderName"] != "WS"]
    # add an index column with new index values
    alert_df = alert_df.reset_index(drop=True)
    # add an column called index with the index values
    alert_df["index"] = alert_df.index
    # convert the dataframe to a JSON object
    alert_json = alert_df.to_json(orient="records")
    # return the JSON object
    return alert_json


def alert_info():
    '''Get basic summary stats from the alerts'''
    # get the JSON object from the NWS API
    alert_json = get_alerts()
    # keep the severity, certainty, and last two characters of the senderName as a pandas dataframe
    alert_df = pd.DataFrame(
        [
            [
                x["properties"]["severity"],
                x["properties"]["certainty"],
                x["properties"]["senderName"][-2:],
            ]
            for x in alert_json["features"]
        ],
        columns=["severity", "certainty", "senderName"],
    )
    # print the total number of alerts
    print("Total number of alerts: ", len(alert_df))
    # print the number of active alerts from senderName "WS"
    print("National-Level Alerts: ", len(alert_df[alert_df["senderName"] == "WS"]))
    # print the number of active alerts after dropping rows where the senderName is "WS"
    print("State-Level Alerts: ", len(alert_df[alert_df["senderName"] != "WS"]))
    # print number of extreme alerts
    print("Extreme Alerts: ", len(alert_df[alert_df["severity"] == "Extreme"]))
    # print the five states with the most active alerts
    print(
        "States with the most active alerts: \n",
        alert_df["senderName"].value_counts().head(),
    )
