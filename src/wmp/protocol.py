# -*- coding: utf-8 -*-

"""
    wmp.protocol
    ~~~~~~~~~~~~

    Protocol versions and command definition.
"""


WORKER_PROTO_VERSION = b'WMPW01'
MANAGER_PROTO_VERSION = b'WMPM01'


COMMANDS = {
            'READY' : 0x01,
            'WAKE'  : 0x02,
            'GIVE'  : 0x03,
            'TAKE'  : 0x04,
            'NO'    : 0x05,
            'DONE'  : 0x06,
            'STATUS': 0x07,
            'CANCEL': 0x08,
           }
