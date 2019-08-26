"""
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.
"""

from six.moves import xrange

from sympy import symbols, integrate, tan
from sympy.core.cache import clear_cache


def run_integrate():
    x, y = symbols('x y')
    f = (1 / tan(x)) ** 10
    return integrate(f, x)


if __name__ == "__main__":
    run_integrate()
