import click

@click.group()
def {{ cookiecutter.cli_command }}():
    """Enter CLI command for {{ cookiecutter.project_name }}"""
    pass


# TODO: your cli scripts
@{{ cookiecutter.cli_command }}.command("hello_world")
def test_command():
    print("Hello world")