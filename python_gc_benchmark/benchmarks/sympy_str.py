"""
 * Copyright (c) 2014, 2019 IBM Corp. and others
 *
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.
"""

from six.moves import xrange

from sympy import expand, symbols
from sympy.core.cache import clear_cache


def run_str():
    x, y, z = symbols('x y z')
    str(expand((x + 2 * y + 3 * z) ** 30))


if __name__ == "__main__":
    run_str()
