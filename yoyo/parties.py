import click

from yoyo.utils.clients import VegaRestClient
from yoyo.options import grpc_url_option


@click.command()
@grpc_url_option
def parties(grpc_url):
    """List parties."""

    client = VegaRestClient(grpc_url)
    party_response = client.get_parties()
    click.echo(party_response)
