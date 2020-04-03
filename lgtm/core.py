import click

@click.command()
@click.option('--message', '-m', default='LGTM', show_default=True, help='String you want to put on image')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM image generator"""
    lgtm(keyword, message)
    click.echo('lgtm')

def lgtm(keyword, message):
    pass