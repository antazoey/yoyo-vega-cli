import click

from yoyo.utils.clients import GRPCRegion


grpc_url_option = click.option("--grpc-url", default=GRPCRegion.USA.value)
