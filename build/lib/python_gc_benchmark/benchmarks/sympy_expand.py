from six.moves import xrange

from sympy import symbols, expand
from sympy.core.cache import clear_cache


def run_expand():
    x, y, z = symbols('x y z')
    expand((1 + x + y + z) ** 20)


if __name__ == "__main__":
    run_expand()