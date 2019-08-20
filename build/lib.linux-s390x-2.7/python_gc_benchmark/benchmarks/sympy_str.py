from six.moves import xrange

from sympy import expand, symbols
from sympy.core.cache import clear_cache


def run_str():
    x, y, z = symbols('x y z')
    str(expand((x + 2 * y + 3 * z) ** 30))


if __name__ == "__main__":
    run_str()
