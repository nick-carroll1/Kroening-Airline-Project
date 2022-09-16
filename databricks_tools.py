"""Module of tools to perform actions on a databricks cluster"""

# import the necessary libraries
import os
import json
from databricks import sql
from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi

from nws_tools import package_alerts

# define the function that will drop the table alerts if it exists and create a new table called alerts using the JSON returned from the get_alerts() function
def create_and_load_alerts_table():
    """Drop a table, create a new one, and load the alerts"""
    print("Connecting to Databricks...")
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
            print("Table created, querying NWS API...")

            # get the json object from the get_alerts() function
            json_object = package_alerts()

            values = ",".join(
                [
                    f"('{x['severity']}', '{x['certainty']}', '{x['senderName']}')"
                    for x in json.loads(json_object)
                ]
            )
            print("Query complete, loading data into table...")

            cursor.execute(f"INSERT INTO alerts VALUES {values}")

            # print a message that the table was created
            print("Upload successful")
            # print the number of rows in the table
            cursor.execute("SELECT COUNT(*) FROM alerts")
            print(f"Number of rows: {cursor.fetchone()[0]}")
            # print the first 5 rows of the table
            cursor.execute("SELECT * FROM alerts LIMIT 5")
            print("First 5 rows:")
            for row in cursor.fetchall():
                print(row)


# define the function that will return the contents of the alerts table
def get_alerts_table_contents():
    """Get the contents of the alerts table"""
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

            print(f"Number of rows: {len(result)}")


# connect to databricks via SSH using python code via Databricks REST API
def hello_cluster():
    """Check the cluster for its name"""
    api_client = ApiClient(
        host=os.getenv("DATABRICKS_HOST"), token=os.getenv("DATABRICKS_TOKEN")
    )

    clusters_api = ClusterApi(api_client)
    clusters_list = clusters_api.list_clusters()

    print("Cluster name, cluster ID")

    for cluster in clusters_list["clusters"]:
        print(f"{cluster['cluster_name']}, {cluster['cluster_id']}")
