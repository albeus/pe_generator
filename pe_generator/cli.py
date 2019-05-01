# -*- coding: utf-8 -*-

"""Console script for pe_generator."""
import sys
import click

from pe_generator.person import Person


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def validate_user_input(person_data_input):
    """Check for invalid input."""
    # Check row consistency
    #    raise InputError(...)
    pass


@click.command()
@click.option('--input-file', '-i', 
              type=click.Path(exists=True, readable=True),
              default='/dev/stdin', show_default=True,
              help="Input file path. By default it reads from stdin.")
def main(input_file):
    """Person entity generator.

    "Person entities generator" generates Person entities represented as data
    structure like JSON objects.

    \b
    Please enter input and text files with the following format:
      ____________________________________________________
      first_name,surname,age,nationality,favourite_colour
      John,Keynes,29,British,red 
      Sarah,Robinson,54,,blue
      ____________________________________________________

    Empty lines will not be considered.
    """
    if input_file == '/dev/stdin':
        click.secho("Enter/Paste your content. Ctrl-D to save it.", fg='green')

    # Read input
    contents = []
    with open(input_file, 'r') as input_file_obj:
        for line in input_file_obj.readlines():
            if line.strip() == "":  # Remove empty lines
                continue 
            contents.append(line.strip())
    # Discard empty input
    if contents == []:
        click.secho('Empty file given... Quit.', fg='yellow')
        sys.exit(0)
    # Validate input
    try:
        validate_user_input(contents)
    except InputError as err:
        print("Input error: {0}".format(err))

    person = Person(contents)
    person.print_json()


if __name__ == "__main__":
    sys.exit(main())
