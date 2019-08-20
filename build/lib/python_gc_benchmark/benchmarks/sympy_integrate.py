from six.moves import xrange

from sympy import symbols, integrate, tan
from sympy.core.cache import clear_cache


def run_integrate():
    x, y = symbols('x y')
    f = (1 / tan(x)) ** 10
    return integrate(f, x)


if __name__ == "__main__":
    run_integrate()
