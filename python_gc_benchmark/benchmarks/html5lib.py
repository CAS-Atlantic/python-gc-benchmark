"""Wrapper script for testing the performance of the html5lib HTML 5 parser.

The input data is the spec document for HTML 5, written in HTML 5.
The spec was pulled from http://svn.whatwg.org/webapps/index.

Credit to Author collinwinter@google.com (Collin Winter)
"""
from __future__ import with_statement

import io
import os.path

import html5lib
import six


def run_html5lib(html_file):
    html_file.seek(0)
    html5lib.parse(html_file)


if __name__ == "__main__":
    # Get all our IO over with early.
    filename = os.path.join(os.path.dirname(__file__),
                            "data", "w3_tr_html5.html")
    with io.open(filename, "rb") as fp:
        html_file = six.BytesIO(fp.read())

    run_html5lib(html_file)