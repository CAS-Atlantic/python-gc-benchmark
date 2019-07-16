import python_gc_benchmark

VERSION = python_gc_benchmark.__version__

DESCRIPTION = 'Python GC benchmark suite'
CLASSIFIERS = [
    'Intended Audience :: Developers',
]

def main():
    import io
    import os.path
    from setuptools import setup

    with io.open('README.md', encoding="utf8") as fp:
        long_description = fp.read().strip()

    with open('requirements.txt') as f:
        required = f.read().splitlines()

    packages = [
        'python_gc_benchmark',
        'python_gc_benchmark.benchmarks',
        'python_gc_benchmark.benchmarks.data',
        'python_gc_benchmark.benchmarks.data.2to3'
    ]

    data = {
        'pygcbenchmark': ['requirements.txt'],
    }

    options = {
            'name': 'python_gc_benchmark',
            'version': VERSION,
            'author': 'Joannah Nanjekye',
            'author_email': 'jnanjeky@unb.ca',
            'license': 'MIT license',
            'description': DESCRIPTION,
            'classifiers': CLASSIFIERS,
            'long_description': long_description,
            'long_description_content_type': 'text/markdown',
            'packages': packages,
            'package_data': data,
            'entry_points': {
                'console_scripts': ['python_gc_benchmark=python_gc_benchmark.cli:main',]
            },
            'install_requires': ["psutil", "six", required],
    }

    setup(**options)

if __name__ == '__main__':
    main()