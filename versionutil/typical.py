# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from versionutil.core import VersionAtomSequence as S, VersionAtom as A,\
    MinimumVersionAtom as Min, MaximumVersionAtom as Max, _Infinity
from cStringIO import StringIO
from re import compile as regex, VERBOSE

def _re():
    ddd = r'\d+'
    vvv = r'{}(?:\.{})*'.format(ddd, ddd)
    prerel = '(?P<prerel>[abc]|rc)(?P<prerelversion>{})'.format(vvv)
    return (
        '(?P<version>{})\n'.format(vvv) + 
        '(?:{})?\n'.format(prerel) +
        '(?:\\.post(?P<post>{}))?\n'.format(ddd) +''
        '(?:\\.dev(?P<dev>{}))?\n'.format(ddd)
    )

class TypicalVersion(object):
    re = _re()
    regex = regex(re, VERBOSE)
    def __init__(self, versin_string):
        parsed = typical_version(versin_string)
        version, prerel, prerelversion, post, dev = (
            parsed['version'], parsed['prerel'], parsed['prerelversion'],
            parsed['post'], parsed['dev']
        )
        version = S(version.split('.')) if version else S.null
        prerelversion = S(prerelversion.split('.')) if prerel else S.null
        prerel = A(prerel) if prerel else Max.s
        post = A(post) if post else Min.s
        dev = A(dev) if dev else Max.s
        self.version, self.prerel, self.postdev = (
            version, (prerel, prerelversion), (post, dev)
        )
    def __str__(self):
        b = StringIO()
        b.write(self.version.stringify('.'))
        prerel, prerelversion = self.prerel
        if not isinstance(prerel, _Infinity):
            b.write(prerel.value)
            b.write(prerelversion.stringify('.'))
        post, dev = self.postdev
        if not isinstance(post, _Infinity):
            b.write('.post')
            b.write(str(post))
        if not isinstance(dev, _Infinity):
            b.write('.dev')
            b.write(str(dev))
        return b.getvalue()
    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(str(self)))
    def __cmp__(self, other):
        x = self.version, self.prerel, self.postdev
        y = other.version, other.prerel, other.postdev
        return cmp(x, y)

def typical_version(versin_string):
    rv = dict(version='', prerel='', prerelversion='', post='', dev='')
    m = TypicalVersion.regex.search(versin_string)
    if not m:
        return rv
    # rv.update(...) does not work well
    for k, v in m.groupdict().iteritems():
        if v == None:
            continue
        rv[k] = v
    return rv

if __name__ == '__main__':
    raise Exception('making a module executable is a bad habit.')
