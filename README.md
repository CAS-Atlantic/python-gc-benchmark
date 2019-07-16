# python-gc-benchmark

This is a Python Benchmark suite that focuses on Memory Usage. The scenarios have been chosen for memory intensive programs Intended for anyone that wants to analyse memory Usage of different Python versions. 

The suite supports Python 2, Python 3, Pypy 2 and Pypy 3.

## Implementation Criteria

The benchmarks feature programs with large demands for memory and are mostly array intensive programs like scientific computing problems, some games and other general programs that are container intensive.

The main metric considered is the Resident Set Size(RSS) which is the allocated memory for a program. This is chosen because;

+ It is machine-independent. Though programs will use more memory on 64-bit machines than 32-bit machines.
+ Stretches the memory manager as it puts a lot of pressure on it.

## Limitations

The metrics on Resident Set Size seem to over report for multi-threaded programs. In the event that two threads share memory, the reported RSS comprises individual memory usage of this memory for each thread. 

Therefore this metric is unsuitable for Multiprocessing and multi-threaded programs.

## Future work

+ Add other useful commands.
+ Add more Scientific benchmarks.

## Run the benchmarks from source

    git clone http://gitlab.casa.cs.unb.ca/jnanjeky/python_gc_benchmark
    cd python-gc-benchmark
    python setup.py install

    python-gc-benchmark  -o <filename> <benchmark>

    # or:

    python-gc-benchmark  -o <filename> all

## Download from PyPI

    pip install python-gc-benchmark
    python-gc-benchmark -o <filename> <benchmark>

    # or:

    python-gc-benchmark -o <filename> all

## References

https://github.com/nuprl/retic_performance
https://github.com/python/pyperformance
http://www.marinamele.com/7-tips-to-time-python-scripts-and-control-memory-and-cpu-usage