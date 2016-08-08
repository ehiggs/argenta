#!/usr/bin/env python3

from distutils.core import setup

setup(name = 'Argenta',
      version = '0.1',
      description = 'Utilities for dealing with Argenta data',
      license = 'GPLv3',
      author = 'Ewan Higgs',
      author_email = 'ewan_higgs@yahoo.co.uk',
      url = 'https://github.com/ehiggs/argenta',
      packages = ['argenta'],
      scripts = ['bin/format-csv'],
      install_requires = ['pandas']
     )
