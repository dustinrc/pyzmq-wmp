# -*- coding: utf-8 -*-

"""
    wmp.protocol
    ~~~~~~~~~~~~

    Protocol versions and command definition.
"""


WORKER_PROTO_VERSION = b'WMPW01'
MANAGER_PROTO_VERSION = b'WMPM01'


COMMANDS = {
            'READY' : b'\x01',
            'WAKE'  : b'\x02',
            'GIVE'  : b'\x03',
            'TAKE'  : b'\x04',
            'NO'    : b'\x05',
            'DONE'  : b'\x06',
            'STATUS': b'\x07',
            'CANCEL': b'\x08',
           }
