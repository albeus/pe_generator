# Person entities generator

[![Build Status](https://travis-ci.com/albeus/pe_generator.svg?branch=master)](https://travis-ci.com/albeus/pe_generator)
[![TestPypi](https://img.shields.io/badge/latest-TestPypi-brightgreen.svg)](https://test.pypi.org/project/pe-generator/)

"pe_generator" generates Person entities represented as data
structure like JSON objects.

Output example:
```json
{
 "person": [
   {
     "first_name": "John",
     "last_name": "Keynes",
     "age": "29",
     "favourite_colour": "red"
   },
{
     "first_name": "Sarah",
     "last_name": "Robinson",
     "age": "54",
     "favourite_colour": "blue"
   }
 ]
}
```

# Features

* Command line interface POSIX compliant.

* It consumes both direct user input and text files with the following
  format:
  ```csv
  first_name,surname,age,nationality,favourite_colour
  John,Keynes,29,British,red
  Sarah,Robinson,54,,blue
  ```
 
* Configurable "hidden fields": they will be collected but not printed
  (default: hide "nationality").

* Versatile input parser: you can add/remove fields. It will only check for
  consistency between header and rows.

* Repeatable deploy using [Pipenv].


# Requirements

* Python >= 3.5 (Python 2.7 can run it but it's not officially tested)
* [Pipenv] (for development and production deployment)

# Quickstart

1. Install latest version from Pypi:
   ```bash
   pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pe-generator
   ```
2. Run it:
   ```bash
   $ pe_generator --help
   Usage: pe_generator [OPTIONS]
   ...
   ```
   ```bash
   $ pe_generator
   Enter/Paste your content. Ctrl-D to save it.
   ...
   ```
   ```bash
   $ pe_generator -i input.csv
   ...
   ```

# Usage

* Help
  ```bash
  $ pe_generator --help
  Usage: pe_generator [OPTIONS]
  
    Person entity generator.
  
    "Person entities generator" generates Person entities represented as data
    structure like JSON objects.
  
    Please enter input and text files with the following format:
      ____________________________________________________
      first_name,surname,age,nationality,favourite_colour
      John,Keynes,29,British,red 
      Sarah,Robinson,54,,blue
      ____________________________________________________
  
    Empty lines will not be considered.
  
  Options:
    -i, --input-file PATH  Input file path. By default, it reads from stdin.
                           [default: /dev/stdin]
    --help                 Show this message and exit.
  ```

# Production deployment

To ensure full reproducibility the program is distributed together with Pipenv
files. To deploy it using a well-tested environment:

1. Ensure having pipenv installed (see [Pipenv installation]).
1. Install "locked" requirements:
   ```bash
   ~:$ git clone https://github.com/albeus/pe_generator.git
   ~:$ cd pe_generator
   pe_generator:$ pipenv install --ignore-pipfile
   ```

# Development

To have a working development environment:

1. Ensure having pipenv installed (see [Pipenv installation]).
1. Install development requirements:
   ```bash
   ~:$ git clone https://github.com/albeus/pe_generator.git
   ~:$ cd pe_generator
   pe_generator:$ pipenv install --dev
   ```

You can use Make:
```bash
  pe_generator:$ pipenv run make
  clean                remove all build, test, coverage and Python artifacts
  clean-build          remove build artifacts
  clean-pyc            remove Python file artifacts
  clean-test           remove test and coverage artifacts
  lint                 check style with flake8
  test                 run tests quickly with the default Python
  release              package and upload a release
  dist                 builds source and wheel package
  install              install package in your system
```

To run tests:
```bash
  pe_generator:$ pipenv run make test
  ...
```

# Author

Alberto Eusebi <alberto.eusebi@albeus.eu>.


[Pipenv]:https://docs.pipenv.org/en/latest/
[Pipenv installation]:https://github.com/pypa/pipenv#installation
