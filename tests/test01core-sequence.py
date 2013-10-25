#!/usr/bin/env python

# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from unittest import TestCase, TestProgram

from transitivity import cmp_abc, cmp_abc_expected, transitivity
import pythonpath
from versionutil.core import VersionAtomSequence as S,\
    MinimumVersionAtom as Min, MaximumVersionAtom as Max

data0 = r'''
1
10
010
1,01
1,10
1,01,10
1,10,01
1,abc,01
'''[1:].splitlines()
class T0Repr(TestCase):
    def test00(self):
        expected = (
            'VersionAtomSequence(' + 
                'MinimumVersionAtom.s, MaximumVersionAtom.s' + 
            ')'
        )
        got = repr(S((Min.s, Max.s)))
        self.assertEquals(expected, got)
    def test01(self):
        data = tuple(s.split(',') for s in data0)
        his_name = S.__name__
        expected = tuple(
            '{}({})'.format(his_name, ', '.join(repr(a) for a in s))
            for s in data
        )
        got = tuple(repr(S(s)) for s in data)
        self.assertEquals(expected, got)

class T1Cmp(TestCase):
    def test00(self):
        expected = cmp_abc_expected
        got = cmp_abc(S(('01',)), S(('010',)), S(('02',)))
        self.assertEquals(expected, got)
    def test01(self):
        data = ('01',), ('010',), ('02',), (1,), (1, 1)
        self.assertTrue(transitivity(S(s) for s in data))
    def test02(self):
        expected = cmp_abc_expected
        got = cmp_abc(S(('01',)), S(('010',)), S.null)
        self.assertEquals(expected, got)

if __name__ == '__main__':
    TestProgram()
