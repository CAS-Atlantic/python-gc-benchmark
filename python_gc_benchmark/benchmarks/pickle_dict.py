"""
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.

Benchmark pickle dict

Credit "collinwinter@google.com (Collin Winter)"
"""

from __future__ import division

import datetime
import random
import sys

import six
from six.moves import xrange
if six.PY3:
    long = int


DICT = {
    'ads_flags': long(0),
    'age': 18,
    'birthday': datetime.date(1980, 5, 7),
    'bulletin_count': long(0),
    'comment_count': long(0),
    'country': 'BR',
    'encrypted_id': 'G9urXXAJwjE',
    'favorite_count': long(9),
    'first_name': '',
    'flags': long(412317970704),
    'friend_count': long(0),
    'gender': 'm',
    'gender_for_display': 'Male',
    'id': long(302935349),
    'is_custom_profile_icon': long(0),
    'last_name': '',
    'locale_preference': 'pt_BR',
    'member': long(0),
    'tags': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    'profile_foo_id': long(827119638),
    'secure_encrypted_id': 'Z_xxx2dYx3t4YAdnmfgyKw',
    'session_number': long(2),
    'signup_id': '201-19225-223',
    'status': 'A',
    'theme': 1,
    'time_created': long(1225237014),
    'time_updated': long(1233134493),
    'unread_message_count': long(0),
    'user_group': '0',
    'username': 'collinwinter',
    'play_count': long(9),
    'view_count': long(7),
    'zip': ''}

TUPLE = (
    [long(x) for x in
        [265867233, 265868503, 265252341, 265243910, 265879514,
         266219766, 266021701, 265843726, 265592821, 265246784,
         265853180, 45526486, 265463699, 265848143, 265863062,
         265392591, 265877490, 265823665, 265828884, 265753032]], 60)


def mutate_dict(orig_dict, random_source):
    new_dict = dict(orig_dict)
    for key, value in new_dict.items():
        rand_val = random_source.random() * sys.maxsize
        if isinstance(key, six.integer_types + (bytes, six.text_type)):
            new_dict[key] = type(key)(rand_val)
    return new_dict


random_source = random.Random(5)  # Fixed seed.
DICT_GROUP = [mutate_dict(DICT, random_source) for _ in range(3)]

MICRO_DICT = dict((key, dict.fromkeys(range(10))) for key in xrange(100))


def run_pickle_dict(loops, pickle, options):
    range_it = xrange(loops)

    protocol = pickle.HIGHEST_PROTOCOL
    obj = MICRO_DICT

    for _ in range_it:
        # 5 dumps dict
        pickle.dumps(obj, protocol)
        pickle.dumps(obj, protocol)
        pickle.dumps(obj, protocol)
        pickle.dumps(obj, protocol)
        pickle.dumps(obj, protocol)

def is_module_accelerated(module):
    return getattr(pickle.Pickler, '__module__', '<jython>') == 'pickle'

if __name__ == "__main__":

    if six.PY2:
        import cPickle as pickle
    elif six.PY3:
        import pickle
        sys.modules['_pickle'] = None
    else:
        import pickle
        if is_module_accelerated(pickle):
            raise RuntimeError("Missing C accelerators for pickle")

    run_pickle_dict(20, pickle, None)
