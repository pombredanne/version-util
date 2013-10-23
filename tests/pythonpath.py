# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from os.path import dirname, join, pardir
from sys import path as pythonpath
pythonpath[:0] = join(dirname(__file__), pardir, 'impl'),

if __name__ == '__main__':
    raise Exception('making a module executable is a bad habit.')
