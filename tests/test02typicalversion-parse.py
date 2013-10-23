#!/usr/bin/env python

# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from unittest import TestCase, TestProgram

import pythonpath
from typicalversion import typical_version, TypicalVersion

expected0 = r'''
(?P<version>\d+(?:\.\d+)*)
(?:(?P<prerel>[abc]|rc)(?P<prerelversion>\d+(?:\.\d+)*))?
(?:\.post(?P<post>\d+))?
(?:\.dev(?P<dev>\d+))?
'''[1:]
class T0Re(TestCase):
    def test(self):
        expected = expected0
        got = TypicalVersion.re
        self.assertEquals(expected, got)

class T1Match(TestCase):
    def test00(self):
        str = 'a1b'
        expected = expect(version='1')
        got = typical_version(str)
        self.assertEquals(expected, got)
    def test01(self):
        str = '1a'
        expected = expect(version='1')
        got = typical_version(str)
        self.assertEquals(expected, got)
    def test02(self):
        str = '1.2b'
        expected = expect(version='1.2')
        got = typical_version(str)
        self.assertEquals(expected, got)
    def test03(self):
        str = '1.2.3c'
        expected = expect(version='1.2.3')
        got = typical_version(str)
        self.assertEquals(expected, got)
    def test04(self):
        str = '1.2.3c4'
        expected = expect(version='1.2.3', prerel='c', prerelversion='4')
        got = typical_version(str)
        self.assertEquals(expected, got)
    def test05(self):
        str = '1.2.3rc4.5.post06.dev07'
        expected = expect(version='1.2.3', prerel='rc', prerelversion='4.5',
            post='06', dev='07',
        )
        got = typical_version(str)
        self.assertEquals(expected, got)
    def test06(self):
        str = ''
        expected = expect()
        got = typical_version(str)
        self.assertEquals(expected, got)

def expect(**kwargs):
    rv = dict(version='', prerel='', prerelversion='', post='', dev='')
    rv.update(kwargs)
    return rv

if __name__ == '__main__':
    TestProgram()
