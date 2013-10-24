#!/usr/bin/env python

# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from unittest import TestCase, TestProgram

import pythonpath
from versionutil.typicalversion import TypicalVersion as V
from versionutil.versioncore import\
    MinimumVersionAtom as Min, MaximumVersionAtom as Max,\
    VersionAtomSequence as S, VersionAtom as A

class T(TestCase):
    def test00(self):
        expected = S.null, (Max.s, S.null), (Min.s, Max.s)
        v = V('')
        got = v.version, v.prerel, v.postdev
        self.assertEquals(expected, got)
    def test01(self):
        expected = S((0, 1, 2)), (A('a'), S(('03', 4))), (A(5), A('06'))
        v = V('0.1.2a03.4.post5.dev06')
        got = v.version, v.prerel, v.postdev
        self.assertEquals(expected, got)

if __name__ == '__main__':
    TestProgram()
