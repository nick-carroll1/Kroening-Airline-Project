from databricks_tools import query_and_load
from nws_tools import response_transform
import click

# build click group
@click.group()
def cli():
    """This is a CLI for the nws_tools and databricks_tools modules."""
    pass


# build click command
@click.command("query")
def query():
    """This command will query the NWS API and load the results into a table in Databricks."""
    query_and_load()


# build click command
@click.command("alerts")
def alerts():
    """This command will query the NWS API and return a count of the total."""
    response_transform()


# run the click command
if __name__ == "__main__":
    cli.add_command(query)
    cli.add_command(alerts)
    cli()
