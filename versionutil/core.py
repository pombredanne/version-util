# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from numbers import Integral

#class VersionAtomSequence(tuple): may be impossible
class VersionAtomSequence(object):
    def __init__(self, iterable):
        def atom(value):
            if isinstance(value, _Infinity):
                return value
            try:
                value = IntegralVersionAtom(value)
            except ValueError:
                value = VersionAtom(value)
            return value
        self.values = tuple(atom(value) for value in iterable)
    def __repr__(self):
        def to_repr(atom):
            return atom if isinstance(atom, _Infinity) else str(atom)
        values = ', '.join(repr(to_repr(atom)) for atom in self.values)
        return '{}({})'.format(self.__class__.__name__, values)
    def __cmp__(self, other):
        x, y = self.values, other.values
        if len(x) == 0:
            return 0 if len(y) == 0 else 1
        elif len(y) == 0:
            return -1
        return cmp(x, y)
    def stringify(self, sep=None):
        rv = (str(a) for a in self.values)
        return sep.join(rv) if sep else sep
VersionAtomSequence.null = VersionAtomSequence(())

class VersionAtom(object):
    def __init__(self, value):
        self.value = str(value)
    def __str__(self):
        return self.value
    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(str(self)))
    def __cmp__(self, other):
        # TODO: clarify
        if isinstance(other, _Infinity):
            return -cmp(other, self)
        compat = isinstance(other, self.__class__)
        return cmp(self.value, other.value) if compat else -1
    def __str__(self):
        return self.value

class _Infinity(VersionAtom):
    def __repr__(self):
        return self.__class__.__name__ + '.s'

class MinimumVersionAtom(_Infinity):
    def __init__(self):
        super(MinimumVersionAtom, self).__init__('')
    def __cmp__(self, other):
        return 0 if type(self) == type(other) else -1
MinimumVersionAtom.s = MinimumVersionAtom()

class MaximumVersionAtom(_Infinity):
    def __init__(self):
        super(MaximumVersionAtom, self).__init__('INFINITY')
    def __cmp__(self, other):
        return 0 if type(self) == type(other) else 1
MaximumVersionAtom.s = MaximumVersionAtom()

class IntegralVersionAtom(VersionAtom):
    def __init__(self, value):
        if isinstance(value, Integral):
            value = str(value)
        else:
            int(value) # or ValueError
            value = str(value)
        super(IntegralVersionAtom, self).__init__(value)
    def __cmp__(self, other):
        if isinstance(other, _Infinity):
            return -cmp(other, self)
        x, y = self.value, other.value
        if x[0] != '0' and y[0] != '0':
            x, y = int(x), int(y)
        return cmp(x, y)

if __name__ == '__main__':
    raise Exception('making a module executable is a bad habit.')
