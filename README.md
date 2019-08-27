<!--
Copyright (c) 2016, 2019 IBM Corp. and others

This program and the accompanying materials are made available under
the terms of the Eclipse Public License 2.0 which accompanies this
distribution and is available at https://www.eclipse.org/legal/epl-2.0/
or the Apache License, Version 2.0 which accompanies this distribution and
is available at https://www.apache.org/licenses/LICENSE-2.0.
-->

# python-gc-benchmark

This is a Python Benchmark suite that focuses on Memory Usage and Heap Analysis. The micro-benchmarks
have been chosen for memory intensive programs Intended for anyone that wants to analyse memory Usage
of different Python versions.

The suite supports Python 2, Python 3, Pypy 2 and Pypy 3.

## Implementation Criteria

The benchmarks feature programs with large demands for memory and are mostly array intensive programs like scientific
computing problems, some games and other general programs that are container intensive.

The memory Information analysed by the suite include:

+ RSS
+ VMS
+ Shared Memory
+ USS and
+ PSS
+ Heap Analysis

The main metric considered is the Resident Set Size(RSS) which is the allocated memory
for a program. This is chosen because;

+ It is machine-independent. Though programs will use more memory on 64-bit machines than
32-bit machines.
+ Stretches the memory manager as it puts a lot of pressure on it.

## Limitations

The metrics on Resident Set Size seem to over report for multi-threaded programs. In the event that
two threads share memory, the reported RSS comprises individual memory usage of this memory for each thread.

Therefore this metric is unsuitable for Multiprocessing and multi-threaded programs. Consider other metrics
other that RSS in these scenarios.

The suite should be launched on Python 3 but benchmarks will be run with the specified Python version available
as an option.

## Run the benchmarks from source

Get the source code:

    git clone http://gitlab.casa.cs.unb.ca/jnanjeky/python_gc_benchmark
    cd python-gc-benchmark

    ## Install dependencies for both Python 2 and 3
    pip install -r requirements.txt

    # Benchmark suite uses Python3
    python3 setup.py install

Run a specific benchmark:

    python-gc-benchmark run -p <python version> -b <benchmark>

View the heap:

    python-gc-benchmark heap -p <python version> -b <benchmark>

View objects on the heap not reachable from the roots after GC :

    python-gc-benchmark heapu -p <python version> -b <benchmark>

Run all benchmarks:

    python-gc-benchmark run -p <python version>

## Download from PyPI

Use pip to install the package:

    pip install python-gc-benchmark

Run a specific benchmark:

    python-gc-benchmark run -p <python version> -b <benchmark>

Run all benchmarks:

    python-gc-benchmark run -p <python version>

## Examples

Let us run some sample benchmarks :

Python 2 :

    gitpod /workspace/python-gc-benchmark $ python-gc-benchmark run -p python2 -b python_gc_benchmark/benchmarks/2to3.py
    Memory Benchmark for : python_gc_benchmark/benchmarks/2to3.py
            RSS:     786432 kb
            VMS:    5582848 kb
            Shared:     720896 kb
            Data:     323584 kb
            USS:     126976 kb
            PSS:     192512 kb

Python 3 :

    gitpod /workspace/python-gc-benchmark $ python-gc-benchmark run -p python3 -b python_gc_benchmark/benchmarks/2to3.py
    Memory Benchmark for : python_gc_benchmark/benchmarks/2to3.py
            RSS:     794624 kb
            VMS:    5582848 kb
            Shared:     729088 kb
            Data:     323584 kb
            USS:     126976 kb
            PSS:     192512 kb


And now, Heap Analysis :

    gitpod /workspace/python-gc-benchmark $ python-gc-benchmark heap -p python3 -b python_gc_benchmark/benchmarks/2to3.py
    Partition of a set of 16 objects. Total size = 1952 bytes.
    Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
        0      1   6      496  25       496  25 types.FrameType
        1      1   6      240  12       736  38 dict of _io.FileIO
        2      1   6      240  12       976  50 dict of psutil.Popen
        3      1   6      240  12      1216  62 dict of subprocess.Popen
        4      1   6      176   9      1392  71 _io.BufferedReader
        5      2  12      128   7      1520  78 tuple
        6      1   6       80   4      1600  82 psutil._pslinux.Process
        7      1   6       72   4      1672  86 _io.FileIO
        8      1   6       56   3      1728  89 psutil.Popen
        9      1   6       56   3      1784  91 subprocess.Popen
    <4 more rows. Type e.g. '_.more' to view.>

Finally, Heap Analysis After Garbage Collection :

    gitpod /workspace/python-gc-benchmark $ python-gc-benchmark heapu -p python3 -b python_gc_benchmark/benchmarks/2to3.py
    Data from unreachable objects.
    Partition of a set of 741 objects. Total size = 171990 bytes.
    Index  Count   %     Size   % Cumulative  % Type
        0     83  11    77848  45     77848  45 dict
        1     46   6    39744  23    117592  68 type
        2     50   7    11200   7    128792  75 set
        3    124  17     9920   6    138712  81 types.WrapperDescriptorType
        4    116  16     9280   5    147992  86 builtins.weakref
        5     94  13     6768   4    154760  90 types.BuiltinMethodType
        6     92  12     5608   3    160368  93 tuple
        7     55   7     3960   2    164328  96 types.MethodDescriptorType
        8     53   7     3816   2    168144  98 types.MemberDescriptorType
        9     14   2     2166   1    170310  99 str
    <6 more rows. Type e.g. '_.more' to view.>

## Future work

+ Add other useful commands.
+ Add more Scientific benchmarks.
+ Investigate Ubuntu s390x .

## References

https://github.com/nuprl/retic_performance

https://github.com/python/pyperformance

http://www.marinamele.com/7-tips-to-time-python-scripts-and-control-memory-and-cpu-usage

(c) Copyright IBM Corp. 2019
