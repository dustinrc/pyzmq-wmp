# -*- coding: utf-8 -*-

"""
    wmp.worker
    ~~~~~~~~~~

    Implements the worker portion of the protocol.
"""


import zmq
from zmq.eventloop.zmqstream import ZMQStream
from zmq.eventloop.ioloop import IOLoop
import protocol


PROTO_VERSION = protocol.WORKER_PROTO_VERSION


class Worker(object):

    def __init__(endpoints):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        ioloop = IOLoop.instance()
        self.endpoints = endpoints
        self.stream = ZMQStream(socket, ioloop)
        self.stream.on_recv(self._on_message)
        self.stream.socket.setsocketopt(zmq.LINGER, 0)
        for endpoint in endpoints:
            self.stream.connect(endpoint)
        self._send_ready()
