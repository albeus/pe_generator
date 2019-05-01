# -*- coding: utf-8 -*-

"""Main module."""

import csv
import json
from collections import OrderedDict


class Person():
    """ Person main class. """
    def __init__(self, person_data_input):
        """ Initialize person instance """
        self.person_data_input = person_data_input
        self.person_data = [row for row in csv.DictReader(self.person_data_input)]
        self.fields_blacklist = ['nationality']
        self.person_data_whitelist = self._exclude_hidden()

    def _exclude_hidden(self):
        """ Get person data except hidden fields """
        person_data_whitelist = []
        for row in self.person_data:
            person_data_whitelist += [OrderedDict([item for item in row.items()
                                      if item[0] not in self.fields_blacklist])]
        return person_data_whitelist

    def data_whitelist_to_json(self):
        """Return person data whitelisted as JSON"""
        return json.dumps({'person': self.person_data_whitelist}, 
                          sort_keys=True, indent=4)

    def print_json(self):
        """ Print person data in structured way."""
        print(self.data_whitelist_to_json())
