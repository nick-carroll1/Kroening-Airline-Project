from databricks_tools import (
    create_and_load_alerts_table,
    get_alerts_table_contents,
    hello_cluster,
)
from nws_tools import alert_info
import click

# build click group
@click.group()
def cli():
    """This is a CLI for the nws_tools and databricks_tools modules. It has functions to query for actice weather alerts, receive summary stats, and load the query payload into a databricks cluster."""


# build click command
@click.command("load_alerts_to_cluster")
def load_alerts():
    """This command will query the NWS API and load the results into a table in Databricks."""
    create_and_load_alerts_table()


# build click command
@click.command("alerts_table_contents")
def alerts_contents():
    """This will query the databricks cluster and tell you the alerts currently loaded."""
    get_alerts_table_contents()


# build click command
@click.command("hello_cluster")
def cluster_wake():
    """This command will wake-up the databricks cluster if it is sleeping and give you basic info about it."""
    hello_cluster()


# build click command
@click.command("NWS_alerts_info")
def all_alert_info():
    """Return basic stats about current weather alerts."""
    alert_info()


# run the click command
if __name__ == "__main__":
    cli.add_command(load_alerts)
    cli.add_command(alerts_contents)
    cli.add_command(cluster_wake)
    cli.add_command(all_alert_info)
    cli()
