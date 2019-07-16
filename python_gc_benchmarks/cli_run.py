#! /usr/bin/env python
"""
Usage: cli.py [-o filename] command [args...]

Runs a subprocess, and measure its RSS (resident set size) every second.
At the end, print the maximum RSS measured, and some statistics.

Also writes "filename", reporting every second the RSS.  If filename is not
given, the output is written to "memusage.log"
"""

import sys, os, re, time, six
from utils import cmd_run

list_of_benchmarks = [
    'benchmarks/2to3.py',
    'benchmarks/call_method.py',
    'benchmarks/call_method_slots.py',
    'benchmarks/call_simple.py',
    'benchmarks/chaos.py',
    'benchmarks/crypo_pyaes.py',
    'benchmarks/deltablue.py',
    'benchmarks/dulwich_log.py',
    'benchmarks/fannkuch.py',
    'benchmarks/float.py',
    'benchmarks/genshi_text.py',
    'benchmarks/genshi_xml.py',
    'benchmarks/go.py',
    'benchmarks/hexiom.py',
    'benchmarks/json_dumps.py',
    'benchmarks/json_loads.py',
    'benchmarks/logging_format.py',
    'benchmarks/logging_silent.py',
    'benchmarks/logging_simple.py',
    'benchmarks/mdp.py',
    'benchmarks/meteor_contest.py',
    'benchmarks/nbody.py',
    'benchmarks/_numpy.py',
    'benchmarks/nqueens.py',
    'benchmarks/pathlib.py',
    'benchmarks/pickle_dict.py',
    'benchmarks/pickle_list.py',
    'benchmarks/pickle.py',
    'benchmarks/pidigits.py',
    'benchmarks/pyflate.py',
    'benchmarks/pystone.py',
    'benchmarks/raytrace.py',
    'benchmarks/regex_compile.py',
    'benchmarks/regex_dna.py',
    'benchmarks/regex_effbot.py',
    'benchmarks/regex_v8.py',
    'benchmarks/richards.py',
    'benchmarks/scimark_fft.py',
    'benchmarks/scimark_lu.py',
    'benchmarks/scimark_monte_carlo.py',
    'benchmarks/scimark_sor.py',
    'benchmarks/scimark_sparse_mat_mult.py',
    'benchmarks/spectra_norm.py',
    'benchmarks/sqlalchemy_declarative.py',
    'benchmarks/sqlalchemy_imperative.py',
    'benchmarks/sqlite_synth.py',
    'benchmarks/sympy_expand.py',
    'benchmarks/sympy_integrate.py',
    'benchmarks/sympy_str.py',
    'benchmarks/sympy_sum.py',
    'benchmarks/telco.py',
    'benchmarks/unpack_sequence.py',
]


def parse_args():
    args = sys.argv[1:]
    if args[0] == '-o':
        args.pop(0)
        outname = args.pop(0)
    else:
        outname = 'memusage.log'
    args[0]

    return outname, args

def _main():
    try:
        outname, args = parse_args()
    except IndexError:
        print >> sys.stderr, __doc__.strip()
        sys.exit(2)
    if args == ['all']:
        args = list_of_benchmarks
        for benchmark in args:
            cmd_run(outname, [benchmark])
    else:
        for benchmark in args:
            cmd_run(outname, [benchmark])

def main():
    try:
        _main()
    except KeyboardInterrupt:
        print("Benchmark suite interrupted: exit!")
    sys.exit(1)


if __name__ == '__main__':
    main()
