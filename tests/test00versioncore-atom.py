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
from versionutil.versioncore import IntegralVersionAtom as A,\
    MinimumVersionAtom as Min, MaximumVersionAtom as Max

class T0Sanity(TestCase):
    def test00(self):
        self.assertRaises(ValueError, A, '3.14')

class T1Create(TestCase):
    def test00accept_int(self):
        expected = '1', '23'
        got = tuple(A(int(s)).value for s in expected)
        self.assertEquals(expected, got)
    def test01leading_zeroes(self):
        expected = '010'
        got = A('010').value
        self.assertEquals(expected, got)

class T2StrRepr(TestCase):
    def test00str00normal(self):
        expected = '1', '23', '010'
        got = tuple(str(A(s)) for s in expected)
        self.assertEquals(expected, got)
    def test00str01inf(self):
        expected = '', 'INFINITY'
        got = tuple(str(a) for a in (Min.s, Max.s))
        self.assertEquals(expected, got)
    def test01repr00normal(self):
        expected = (
            "IntegralVersionAtom('1')",
            "IntegralVersionAtom('23')",
            "IntegralVersionAtom('010')",
        )
        got = tuple(repr(A(s)) for s in ('1', '23', '010'))
        self.assertEquals(expected, got)
    def test01repr01inf(self):
        expected = 'MinimumVersionAtom.s', 'MaximumVersionAtom.s'
        got = tuple(repr(a) for a in (Min.s, Max.s))
        self.assertEquals(expected, got)

class T3Cmp(TestCase):
    def test00(self):
        expected = cmp_abc_expected
        got = cmp_abc(A('01'), A(2), A(10))
        self.assertEquals(expected, got)
    def test01(self):
        data = (
            Min.s,
            A(0),
            A('01'), A('010'), A('02'), A('020'),
            A(1), A(2), A(10), A(20), A(999),
            Max.s,
        )
        self.assertTrue(transitivity(data))

if __name__ == '__main__':
    TestProgram()
