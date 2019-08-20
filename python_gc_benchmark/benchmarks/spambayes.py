
"""
 * Copyright (c) 2014, 2019 IBM Corp. and others
 *
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.
"""

"""Wrapper script for testing the performance of SpamBayes.

Run a canned mailbox through a SpamBayes ham/spam classifier.

Credit:

__author__ = "skip.montanaro@gmail.com (Skip Montanaro)"
__contact__ = "collinwinter@google.com (Collin Winter)"

"""

import os.path

from spambayes import hammie, mboxutils


def run_spambayes(ham_classifier, messages):
    for msg in messages:
        ham_classifier.score(msg)


if __name__ == "__main__":
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    mailbox = os.path.join(data_dir, "spambayes_mailbox")
    ham_data = os.path.join(data_dir, "spambayes_hammie.pkl")
    messages = list(mboxutils.getmbox(mailbox))
    ham_classifier = hammie.open(ham_data, "pickle", "r")

    run_spambayes(ham_classifier, messages)
