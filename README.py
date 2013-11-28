#!/usr/bin/env python

# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

# installation:
# $ sudo mkdir --parent /opt/lib/x19290/py
# $ sudo cp --recursive $PWD /opt/lib/x19290/py/
# $ python README.py

# see https://wiki.python.org/moin/Distutils/VersionComparison
r'''
>>> from sys import path as pythonpath
>>> pythonpath[:0] = '/opt/lib/x19290/py/version-util',
>>> from versionutil.typical import TypicalVersion as V
>>> (V('1.0a1')
...  < V('1.0a2.dev456')
...  < V('1.0a2')
...  < V('1.0a2.1.dev456')  # e.g. need to do a quick post release on 1.0a2
...  < V('1.0a2.1')
...  < V('1.0b1.dev456')
...  < V('1.0b2')
...  < V('1.0c1.dev456')
...  < V('1.0c1')
...  < V('1.0.dev456')
...  < V('1.0')
...  < V('1.0.post456'))
True
'''

if __name__ == '__main__':
    from doctest import testmod
    testmod()
