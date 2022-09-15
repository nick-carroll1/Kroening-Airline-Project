# select all items from a databricks table called "squares"

# import the necessary libraries
import os
import requests
import json

# define the function that will return the contents of a Databricks cluster
def get_databricks_cluster_contents():
    # define the URL for the Databricks cluster
    url = os.getenv("DATABRICKS_HOST")
    # define the headers for the Databricks cluster
    headers = {"Authorization": "Bearer " + os.getenv("DATABRICKS_TOKEN")}
    # send the JSON object to the Databricks cluster
    response = requests.get(url, headers=headers)
    # return the response from the Databricks cluster
    return response


# print the contents of the Databricks cluster
print(get_databricks_cluster_contents())

# select all items from a databricks table called "squares"
