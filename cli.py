import click

@click.group()
def cli():
    pass


@cli.command()
@click.option(' =delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) :
"""Готовит и доставляет пиццу"""

@cli.command()
def menu():
"""Выводит меню"""



if __name__ == '__main__' :
    cli()