import click

from internal.schema import Session, Context


@click.group()
def cli():
    pass


@cli.group()
def context():
    pass


@context.command("list")
def get_contexts():
    session = Session()
    contexts = session.query(Context).all()

    for context in contexts:
        click.echo(f"{context.id} | {context}")


@context.command("create")
@click.argument("name")
@click.argument("color", required=False)
def create_context(name, color):
    session = Session()
    new_context = Context(name=name, color=color if color else "red")
    session.add(new_context)
    session.commit()

    click.echo("Context '{}' added successfully".format(name))


@context.command("update")
@click.argument("id")
@click.option("--name")
@click.option("--color")
def update_context(id, name, color):
    if name is None and color is None:
        click.echo("Please specify a field to update [name, color]")
        return
    click.echo(f"Inputs | ID: {id}, Name: {name}, Color: {color}")
    session = Session()
    to_update = session.query(Context).filter(Context.id == id).first()

    if to_update:
        click.echo(f"{to_update.id} | {to_update}")
        update_name = name is not None and to_update.name != name
        update_color = color is not None and to_update.color != color

        if not update_name and not update_color:
            click.echo("Fields designated already equal provided values")
            return

        if update_name:
            click.echo(f"{to_update.name} => {name}")
            to_update.name = name

        if update_color:
            click.echo(f"{to_update.color} => {color}")
            to_update.color = color

        session.commit()

    else:
        click.echo(f"Context '{id}' not found")


@context.command("delete")
@click.argument("id")
def delete_context(id):
    click.echo(f"Inputs | ID: {id}")
    session = Session()
    to_delete = session.query(Context).filter(Context.id == id).first()

    if not to_delete:
        click.echo(f"Context '{id}' not found")
        return

    session.delete(to_delete)
    session.commit()
    click.echo(f"'{to_delete}' removed")


if __name__ == "__main__":
    cli()
