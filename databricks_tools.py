# use nws_tools.py to get the alerts
# tell databricks to drop the table alerts if it exists
# tell databricks to create a table called alerts
# tell databricks to insert the alerts into the table

# import the necessary libraries
from optparse import Values
import os
import requests
import json
from databricks import sql
from nws_tools import response_transform

# define the function that will drop the table alerts if it exists and create a new table called alerts using the JSON returned from the get_alerts() function
def create_alerts_table():
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute("DROP TABLE IF EXISTS alerts")

            cursor.execute(
                "CREATE TABLE alerts (severity string, certainty string, senderName string)"
            )

            # get the json object from the get_alerts() function
            json_object = response_transform()

            values = ",".join(
                [
                    f"('{x['severity']}', '{x['certainty']}', '{x['senderName']}')"
                    for x in json.loads(json_object)
                ]
            )

            cursor.execute(f"INSERT INTO alerts VALUES {values}")


# define the function that will return the contents of the alerts table
def get_alerts_table_contents():
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM alerts")

            result = cursor.fetchall()

            for row in result:
                print(row)


# define a function to run the create_alerts_table() function and the get_alerts_table_contents() function
def query_and_load():
    create_alerts_table()
    get_alerts_table_contents()


if __name__ == "__main__":
    query_and_load()
