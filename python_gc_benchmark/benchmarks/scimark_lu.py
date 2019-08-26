"""
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.
"""

from array import array
import math

from six.moves import xrange


class Array2D(object):

    def __init__(self, w, h, data=None):
        self.width = w
        self.height = h
        self.data = array('d', [0]) * (w * h)
        if data is not None:
            self.setup(data)

    def _idx(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return y * self.width + x
        raise IndexError

    def __getitem__(self, x_y):
        (x, y) = x_y
        return self.data[self._idx(x, y)]

    def __setitem__(self, x_y, val):
        (x, y) = x_y
        self.data[self._idx(x, y)] = val

    def setup(self, data):
        for y in xrange(self.height):
            for x in xrange(self.width):
                self[x, y] = data[y][x]
        return self

    def indexes(self):
        for y in xrange(self.height):
            for x in xrange(self.width):
                yield x, y

    def copy_data_from(self, other):
        self.data[:] = other.data[:]


class Random(object):
    MDIG = 32
    ONE = 1
    m1 = (ONE << (MDIG - 2)) + ((ONE << (MDIG - 2)) - ONE)
    m2 = ONE << MDIG // 2
    dm1 = 1.0 / float(m1)

    def __init__(self, seed):
        self.initialize(seed)
        self.left = 0.0
        self.right = 1.0
        self.width = 1.0
        self.haveRange = False

    def initialize(self, seed):

        self.seed = seed
        seed = abs(seed)
        jseed = min(seed, self.m1)
        if (jseed % 2 == 0):
            jseed -= 1
        k0 = 9069 % self.m2
        k1 = 9069 / self.m2
        j0 = jseed % self.m2
        j1 = jseed / self.m2
        self.m = array('d', [0]) * 17
        for iloop in xrange(17):
            jseed = j0 * k0
            j1 = (jseed / self.m2 + j0 * k1 + j1 * k0) % (self.m2 / 2)
            j0 = jseed % self.m2
            self.m[iloop] = j0 + self.m2 * j1
        self.i = 4
        self.j = 16

    def nextDouble(self):
        I, J, m = self.i, self.j, self.m
        k = m[I] - m[J]
        if (k < 0):
            k += self.m1
        self.m[J] = k

        if (I == 0):
            I = 16
        else:
            I -= 1
        self.i = I

        if (J == 0):
            J = 16
        else:
            J -= 1
        self.j = J

        if (self.haveRange):
            return self.left + self.dm1 * float(k) * self.width
        else:
            return self.dm1 * float(k)

    def RandomMatrix(self, a):
        for x, y in a.indexes():
            a[x, y] = self.nextDouble()
        return a

    def RandomVector(self, n):
        return array('d', [self.nextDouble() for i in xrange(n)])


def copy_vector(vec):
    # Copy a vector created by Random.RandomVector()
    vec2 = array('d')
    vec2[:] = vec[:]
    return vec2


class ArrayList(Array2D):

    def __init__(self, w, h, data=None):
        self.width = w
        self.height = h
        self.data = [array('d', [0]) * w for y in xrange(h)]
        if data is not None:
            self.setup(data)

    def __getitem__(self, idx):
        if isinstance(idx, tuple):
            return self.data[idx[1]][idx[0]]
        else:
            return self.data[idx]

    def __setitem__(self, idx, val):
        if isinstance(idx, tuple):
            self.data[idx[1]][idx[0]] = val
        else:
            self.data[idx] = val

    def copy_data_from(self, other):
        for l1, l2 in zip(self.data, other.data):
            l1[:] = l2


def LU_factor(A, pivot):
    M, N = A.height, A.width
    minMN = min(M, N)
    for j in xrange(minMN):
        jp = j
        t = abs(A[j][j])
        for i in xrange(j + 1, M):
            ab = abs(A[i][j])
            if ab > t:
                jp = i
                t = ab
        pivot[j] = jp

        if A[jp][j] == 0:
            raise Exception("factorization failed because of zero pivot")

        if jp != j:
            A[j], A[jp] = A[jp], A[j]

        if j < M - 1:
            recp = 1.0 / A[j][j]
            for k in xrange(j + 1, M):
                A[k][j] *= recp

        if j < minMN - 1:
            for ii in xrange(j + 1, M):
                for jj in xrange(j + 1, N):
                    A[ii][jj] -= A[ii][j] * A[j][jj]


def LU(lu, A, pivot):
    lu.copy_data_from(A)
    LU_factor(lu, pivot)


def run_LU(cycles, N):
    rnd = Random(7)
    A = rnd.RandomMatrix(ArrayList(N, N))
    lu = ArrayList(N, N)
    pivot = array('i', [0]) * N
    range_it = xrange(cycles)

    for _ in range_it:
        LU(lu, A, pivot)


if __name__ == "__main__":
    run_LU(100, 5)
