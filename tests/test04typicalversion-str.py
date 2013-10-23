#!/usr/bin/env python

# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from unittest import TestCase, TestProgram

from versionstrings import versionstrings
import pythonpath
from typicalversion import TypicalVersion as V

class T0Str(TestCase):
    def test00str(self):
        expected = versionstrings
        got = tuple(str(V(s)) for s in versionstrings)
        self.assertEquals(expected, got)
    def test01repr(self):
        expected = tuple(
            '{}({})'.format(V.__name__, repr(str(s))) for s in versionstrings
        )
        got = tuple(repr(V(s)) for s in versionstrings)
        self.assertEquals(expected, got)

if __name__ == '__main__':
    TestProgram()
