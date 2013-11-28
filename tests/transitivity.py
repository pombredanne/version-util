# Copyright (C) 2013 Hiroki Horiuchi <x19290@gmail.com>
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided
# the copyright notice and this notice are preserved.
# This file is offered as-is, without any warranty.

from itertools import combinations

def cmp_abc(a, b, c):
    return (
        a < b, b < c, a < c, a <= b, b <= c, a <= c, a != b, b != c, a != c,
        a > b, b > c, a > c, a >= b, b >= c, a >= c, a == b, b == c, a == c,
    )

cmp_abc_expected = (
    True, True, True, True, True, True, True, True, True,
    False, False, False, False, False, False, False, False, False,
)

def transitivity(data):
    data = tuple(combinations(data, 2))
    l = len(data)
#     x, y = data[32]
#     z = y < x
    a = tuple(x < y for (x, y) in data)
    b = tuple(x != y for (x, y) in data)
    c = tuple(x == y for (x, y) in data)
    d = tuple(x > y for (x, y) in data)
    e = tuple(y < x for (x, y) in data)
    f = tuple(y != x for (x, y) in data)
    g = tuple(y == x for (x, y) in data)
    h = tuple(y > x for (x, y) in data)
    got = (a, b, c, d, e, f, g, h)
    expected = (
        (True,) * l, (True,) * l, (False,) * l, (False,) * l,
        (False,) * l, (True,) * l, (False,) * l, (True,) * l,
    )
    return expected == got

if __name__ == '__main__':
    raise Exception('making a module executable is a bad habit.')
