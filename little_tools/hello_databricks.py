'''A tool to see a response status from a databricks'''

# import the necessary libraries
import os
import requests

# define the function that will return the response from a Databricks cluster
def get_databricks_response():
    # define the URL for the Databricks cluster
    url = os.getenv("DATABRICKS_HOST")
    # define the headers for the Databricks cluster
    headers = {"Authorization": "Bearer " + os.getenv("DATABRICKS_TOKEN")}
    # send the JSON object to the Databricks cluster
    response = requests.get(url, headers=headers, timeout=5)
    # return the response from the Databricks cluster
    return response


# print the contents of the Databricks cluster
print(get_databricks_response())
