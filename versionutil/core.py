# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from numbers import Integral
from wheels19290 import python_major_version
if 3 <= python_major_version:
    from wheels19290 import cmp

#class VersionAtomSequence(tuple): may be impossible
class VersionAtomSequence(object):
    null = None
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
    def __lt__(self, other):
        x, y = self.values, other.values
        if not x:
            return False
        if not y:
            return True
        return x < y
    def __le__(self, other):
        x, y = self.values, other.values
        if not x:
            return not y
        if not y:
            return True
        return x <= y
    def __gt__(self, other):
        x, y = self.values, other.values
        if not x:
            return y
        if not y:
            return False
        return x > y
    def __ge__(self, other):
        x, y = self.values, other.values
        if not x:
            return True
        if not y:
            return False
        return x >= y
    def __ne__(self, other):
        return not self == other
    def __eq__(self, other):
        return type(self) == type(other) and self.values == other.values
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
    # TODO: clarify
    def __lt__(self, other):
        if isinstance(other, _Infinity):
            return other > self
        compat = isinstance(other, self.__class__)
        return self.value < other.value if compat else True
    def __le__(self, other):
        if isinstance(other, _Infinity):
            return other >= self
        compat = isinstance(other, self.__class__)
        return self.value <= other.value if compat else True
    def __gt__(self, other):
        if isinstance(other, _Infinity):
            return other < self
        compat = isinstance(other, self.__class__)
        return self.value > other.value if compat else False
    def __ge__(self, other):
        if isinstance(other, _Infinity):
            return other <= self
        compat = isinstance(other, self.__class__)
        return self.value >= other.value if compat else False
    def __ne__(self, other):
        return not self == other    
    def __eq__(self, other):
        return type(self) == type(other) and self.value == other.value

class _Infinity(VersionAtom):
    def __repr__(self):
        return self.__class__.__name__ + '.s'
    def __ne__(self, other):
        return not self == other
    def __eq__(self, other):
        return type(self) == type(other)

class MinimumVersionAtom(_Infinity):
    s = None
    def __init__(self):
        super(MinimumVersionAtom, self).__init__('')
    def __lt__(self, other):
        return self != other
    def __le__(self, other):
        return True
    def __gt__(self, other):
        return False
    def __ge__(self, other):
        return self == other
MinimumVersionAtom.s = MinimumVersionAtom()

class MaximumVersionAtom(_Infinity):
    s = None
    def __init__(self):
        super(MaximumVersionAtom, self).__init__('INFINITY')
    def __lt__(self, other):
        return False
    def __le__(self, other):
        return self == other
    def __gt__(self, other):
        return self != other
    def __ge__(self, other):
        return True
MaximumVersionAtom.s = MaximumVersionAtom()

class IntegralVersionAtom(VersionAtom):
    def __init__(self, value):
        if isinstance(value, Integral):
            value = str(value)
        else:
            int(value) # or ValueError
            value = str(value)
        super(IntegralVersionAtom, self).__init__(value)
    def __lt__(self, other):
        if isinstance(other, _Infinity):
            return other > self
        if not isinstance(other, self.__class__):
            return True
        return _int_cmp(self.value, other.value) < 0
    def __le__(self, other):
        if isinstance(other, _Infinity):
            return other >= self
        if not isinstance(other, self.__class__):
            return True
        return _int_cmp(self.value, other.value) <= 0
    def __gt__(self, other):
        if isinstance(other, _Infinity):
            return other < self
        if not isinstance(other, self.__class__):
            return False
        return 0 < _int_cmp(self.value, other.value)
    def __ge__(self, other):
        if isinstance(other, _Infinity):
            return other <= self
        if not isinstance(other, self.__class__):
            return False
        return 0 <= _int_cmp(self.value, other.value)

def _int_cmp(x, y):
    if not (x.startswith('0') or y.startswith('0')):
        x, y = int(x), int(y)
    return cmp(x, y)

if __name__ == '__main__':
    raise Exception('making a module executable is a bad habit.')
