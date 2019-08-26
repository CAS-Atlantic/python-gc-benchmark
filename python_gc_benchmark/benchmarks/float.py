"""
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.

Artificial, floating point-heavy benchmark originally used by Factor.
"""
from six.moves import xrange

from math import sin, cos, sqrt


POINTS = 100000


class Point(object):
    __slots__ = ('x', 'y', 'z')

    def __init__(self, i):
        self.x = x = sin(i)
        self.y = cos(i) * 3
        self.z = (x * x) / 2

    def __repr__(self):
        return "<Point: x=%s, y=%s, z=%s>" % (self.x, self.y, self.z)

    def normalize(self):
        x = self.x
        y = self.y
        z = self.z
        norm = sqrt(x * x + y * y + z * z)
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def maximize(self, other):
        self.x = self.x if self.x > other.x else other.x
        self.y = self.y if self.y > other.y else other.y
        self.z = self.z if self.z > other.z else other.z
        return self


def maximize(points):
    next = points[0]
    for p in points[1:]:
        next = next.maximize(p)
    return next


def run_benchmark(n):
    points = [None] * n
    for i in xrange(n):
        points[i] = Point(i)
    for p in points:
        p.normalize()
    return maximize(points)


if __name__ == "__main__":
    points = POINTS
    run_benchmark(points)
