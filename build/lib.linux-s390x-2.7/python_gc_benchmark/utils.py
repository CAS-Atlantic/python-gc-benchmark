"""
/*******************************************************************************
 * Copyright (c) 2019 Eclipse Foundation and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://eclipse.org/legal/epl-v10.html
 *******************************************************************************/
"""

import sys, os, re, time, six

import psutil
from subprocess import PIPE

gen_bms = [
    'benchmarks/2to3.py',
    'benchmarks/call_method.py',
    'benchmarks/call_method_slots.py',
    'benchmarks/call_simple.py',
    'benchmarks/chaos.py',
    'benchmarks/crypo_pyaes.py',
    'benchmarks/deltablue.py',
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
    'benchmarks/nqueens.py',
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
    'benchmarks/sqlite_synth.py',
]

#only support python3
py3_bms =[
    'benchmarks/sympy_expand.py',
    'benchmarks/sympy_integrate.py',
    'benchmarks/sympy_str.py',
    'benchmarks/sympy_sum.py',
    'benchmarks/unpack_sequence.py',
    'benchmarks/sqlalchemy_declarative.py',
    'benchmarks/sqlalchemy_imperative.py',
    'benchmarks/pickle_dict.py',
    'benchmarks/pickle_list.py',
    'benchmarks/_pickle.py',
]

#only support python 2 -- this though todo work on a work around.
py2_bms =[
    'benchmarks/_pathlib.py',
]

def collect_benchmarks(python_version):
    if python_version == "python3" or "pypy3":
        bms = gen_bms + py3_bms
    else:
        bms = gen_bms + py2_bms
    
    return bms

def run_benchmark(options, benchmark):

    command = "%s" % options.python, "%s" % benchmark

    p = psutil.Popen(command, stdout=PIPE)

    memory_info = p.memory_full_info()

    print ('Memory Benchmark for : %s' %benchmark)
    print ('\tRSS: %10d kb' % memory_info.rss)
    print ('\tVMS: %10d kb' % memory_info.vms)
    print ('\tShared: %10d kb' % memory_info.shared)
    print ('\tData: %10d kb' % memory_info.data)
    print ('\tUSS: %10d kb' % memory_info.uss)
    print ('\tPSS: %10d kb' % memory_info.pss)

def cmd_run(options):

	print("Python GC benchmark Version %s", python_gc_benchmark.__version__)

	if options.benchmark != None:
		run_benchmark(options, options.benchmark)
	elif options.benchmark == None:
        list_of_benchmarks = collect_benchmarks(options.python)
		for bm in list_of_benchmarks:
			run_benchmark(options, bm)