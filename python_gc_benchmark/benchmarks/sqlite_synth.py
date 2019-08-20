"""
 * Copyright (c) 2014, 2019 IBM Corp. and others
 *
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.
"""

"""
SQLite benchmark.

The goal of the benchmark is to test CFFI performance and going back and forth
between SQLite and Python a lot. Therefore the queries themselves are really
simple.
"""

import sqlite3
import math

from six.moves import xrange


class AvgLength(object):

    def __init__(self):
        self.sum = 0
        self.count = 0

    def step(self, x):
        if x is not None:
            self.count += 1
            self.sum += len(x)

    def finalize(self):
        return self.sum / float(self.count)


def run_sqlite(loops):
    conn = sqlite3.connect(":memory:")
    conn.execute('create table cos (x, y, z);')
    for i in xrange(loops):
        cos_i = math.cos(i)
        conn.execute('insert into cos values (?, ?, ?)',
                     [i, cos_i, str(i)])

    conn.create_function("cos", 1, math.cos)
    for x, cosx1, cosx2 in conn.execute("select x, cos(x), y from cos"):
        assert math.cos(x) == cosx1 == cosx2

    conn.create_aggregate("avglength", 1, AvgLength)
    cursor = conn.execute("select avglength(z) from cos;")
    cursor.fetchone()[0]

    conn.execute("delete from cos;")
    conn.close()


if __name__ == "__main__":
    run_sqlite(10)
