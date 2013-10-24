#!/usr/bin/env python

# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from unittest import TestCase, TestProgram

from transitivity import cmp_abc, cmp_abc_expected, transitivity
from versionstrings import a, b, c, versionstrings
import pythonpath
from versionutil.typicalversion import TypicalVersion as V

class T(TestCase):
    def test00(self):
        expected = cmp_abc_expected
        got = cmp_abc(V(a), V(b), V(c))
        self.assertEquals(expected, got)
    def test01(self):
        self.assertTrue(transitivity(V(s) for s in versionstrings))
    def test02anon_is_latest(self):
        self.assertLess(V('jdk8.0'), V('jdk'))

if __name__ == '__main__':
    TestProgram()
