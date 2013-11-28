# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from os.path import dirname, join, pardir
from sys import path as pythonpath
def _prepend():
    upper = join(dirname(__file__), pardir)
    top = join(upper, pardir)
    return upper, join(top, 'testutil-19290'), join(top, 'wheels-19290')
pythonpath[:0] = _prepend()

if __name__ == '__main__':
    raise Exception('making a module executable is a bad habit.')
