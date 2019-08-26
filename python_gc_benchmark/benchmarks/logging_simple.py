"""
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.

Rationale for logging_silent by Antoine Pitrou:
"""

# Python imports
import io
import logging

# Third party imports
import six
from six.moves import xrange

# A simple format for parametered logging
FORMAT = 'important: %s'
MESSAGE = 'some important information to be logged'


def truncate_stream(stream):
    stream.seek(0)
    stream.truncate()

def run_logging_simple(loops, logger, stream):
    truncate_stream(stream)

    # micro-optimization: use fast local variables
    m = MESSAGE
    range_it = xrange(loops)

    for _ in range_it:
        # repeat 10 times
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)
        logger.warning(m)

    lines = stream.getvalue().splitlines()
    if len(lines) != loops * 10:
        raise ValueError("wrong number of lines")


if __name__ == "__main__":

    if six.PY3:
        stream = io.StringIO()
    else:
        stream = io.BytesIO()

    handler = logging.StreamHandler(stream=stream)
    logger = logging.getLogger("benchlogger")
    logger.propagate = False
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)

    run_logging_simple(10, logger, stream)
