# This file is placed in the Public Domain.


"clients"


import unittest


from genocide.clients import Client
from genocide.message import Message, ready, reply, wait


def hello(event):
    reply(event, "hello")
    ready(event)


clt = Client()
clt.register("hello", hello)
clt.start()


class TestHandler(unittest.TestCase):

    def test_loop(self):
        e = Message()
        e.kind = "hello"
        clt.put(e)
        wait(e)
        self.assertTrue(True)
