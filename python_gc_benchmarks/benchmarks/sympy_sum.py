from six.moves import xrange

from sympy import symbols, summation
from sympy.core.cache import clear_cache

def run_sum():
    x, i = symbols('x i')
    summation(x ** i / i, (i, 1, 400))

if __name__ == "__main__":
    run_sum()
