# write a tool that sends a JSON object to a Databricks cluster

# import the necessary libraries
import os
import requests
import json

# define the function that will send the JSON object to the Databricks cluster
def send_json_to_databricks(json_object):
    # define the URL for the Databricks cluster
    url = os.getenv("DATABRICKS_HOST")
    # define the headers for the Databricks cluster
    headers = {"Authorization": "Bearer " + os.getenv("DATABRICKS_TOKEN")}
    # send the JSON object to the Databricks cluster
    response = requests.post(url, headers=headers, json=json_object)
    # return the response from the Databricks cluster
    return response


from nws_tools import get_alerts, main

send_json_to_databricks(get_alerts())
main()
