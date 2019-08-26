"""
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.
"""

from __future__ import print_function
from decimal import ROUND_HALF_EVEN, ROUND_DOWN, Decimal, getcontext, Context
import io
import os
from struct import unpack

import six
from six.moves import xrange


def rel_path(*path):
    return os.path.join(os.path.dirname(__file__), *path)


def run_telco(loops, filename):
    getcontext().rounding = ROUND_DOWN
    rates = list(map(Decimal, ('0.0013', '0.00894')))
    twodig = Decimal('0.01')
    Banker = Context(rounding=ROUND_HALF_EVEN)
    basictax = Decimal("0.0675")
    disttax = Decimal("0.0341")

    with open(filename, "rb") as infil:
        data = infil.read()

    infil = io.BytesIO(data)
    outfil = six.StringIO()

    for _ in range(loops):
        infil.seek(0)

        sumT = Decimal("0")   # sum of total prices
        sumB = Decimal("0")   # sum of basic tax
        sumD = Decimal("0")   # sum of 'distance' tax

        for i in xrange(5000):
            datum = infil.read(8)
            if datum == '':
                break
            n, =  unpack('>Q', datum)

            calltype = n & 1
            r = rates[calltype]

            p = Banker.quantize(r * n, twodig)

            b = p * basictax
            b = b.quantize(twodig)
            sumB += b

            t = p + b

            if calltype:
                d = p * disttax
                d = d.quantize(twodig)
                sumD += d
                t += d

            sumT += t
            print(t, file=outfil)

        outfil.seek(0)
        outfil.truncate()


if __name__ == "__main__":
    filename = rel_path("data", "telco-bench.b")
    run_telco(1, filename)
