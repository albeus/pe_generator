#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pe_generator` package."""

from collections import OrderedDict
from pe_generator import person

# - malformed input
#   - header: empty field
#   - rows: inconsistent number of fields

input_text_good = "\
first_name,surname,age,nationality,favourite_colour\n\
John,Keynes,29,British,red\n\
Sarah,Robinson,54,,blue\n\
"

input_content_good = ['first_name,surname,age,nationality,favourite_colour', 
                      'John,Keynes,29,British,red',
                      'Sarah,Robinson,54,,blue']

csv_data_structure_good = [OrderedDict([('first_name', 'John'),
                                        ('surname', 'Keynes'),
                                        ('age', '29'),
                                        ('nationality', 'British'),
                                        ('favourite_colour', 'red')]),
                           OrderedDict([('first_name', 'Sarah'),
                                        ('surname', 'Robinson'),
                                        ('age', '54'),
                                        ('nationality', ''),
                                        ('favourite_colour', 'blue')])]

json_data_structure_good = '\
{\n\
    "person": [\n\
        {\n\
            "age": "29",\n\
            "favourite_colour": "red",\n\
            "first_name": "John",\n\
            "surname": "Keynes"\n\
        },\n\
        {\n\
            "age": "54",\n\
            "favourite_colour": "blue",\n\
            "first_name": "Sarah",\n\
            "surname": "Robinson"\n\
        }\n\
    ]\n\
}'


def test_import_good_csv():
    """Ensure good csv is properly acquired."""
    test_person = person.Person(input_content_good)
    assert test_person.person_data == csv_data_structure_good


def test_print_json():
    """Check json data structure"""
    test_person = person.Person(input_content_good)
    assert test_person.data_whitelist_to_json() == json_data_structure_good
