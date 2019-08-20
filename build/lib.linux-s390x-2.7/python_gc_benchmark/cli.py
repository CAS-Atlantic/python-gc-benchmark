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
import argparse
import psutil
from subprocess import PIPE
from utils import cmd_run
from shutil import which


def parse_args():
    parser = argparse.ArgumentParser(
        description=("Runs memory usage benchmarks for different"
            "memory intensive programs."))

    subparsers = parser.add_subparsers(dest='action')
    cmds = []

    # run
    cmd = subparsers.add_parser(
        'run', help='Run benchmarks on the running python')
    cmds.append(cmd)
    cmd.add_argument("-o", "--output", metavar="FILENAME",
                     help="output file for benchmark results.")

    for cmd in cmds:
        cmd.add_argument("-p", "--python",
                         help="Python executable (default: use running Python)",
                         default=sys.executable)
        cmd.add_argument("-b", "--benchmark",
                         help="Python executable (default: use running Python)",
                         default=None)

    options = parser.parse_args()

    if not options.action:
        parser.print_help()
        sys.exit(1)

    if hasattr(options, 'python'):
        options.python = os.path.expanduser(options.python)
        abs_python = which(options.python)
        if not abs_python:
            print("ERROR: Unable to locate the Python executable: %r" %
                  options.python)
            sys.exit(1)
        options.python = os.path.realpath(abs_python)

    return (parser, options)

def _main():
    try:
        parser, options = parse_args()
    except IndexError:
        print >> sys.stderr, __doc__.strip()
        sys.exit(2)

    if options.action == 'run':
        cmd_run(options)
        sys.exit(1)

def main():
    try:
        _main()
    except KeyboardInterrupt:
        print("Benchmark suite interrupted: exit!")


if __name__ == '__main__':
    main()
