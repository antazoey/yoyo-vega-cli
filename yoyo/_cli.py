import click

from yoyo.parties import parties


@click.group()
def cli():
    pass


cli.add_command(parties)  # type: ignore
