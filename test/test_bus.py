# This file is placed in the Public Domain.


"bus"


import unittest


from genocide.hdl import Bus, Handler


class Client(Handler):

    gotcha = False

    def __init__(self):
        Handler.__init__(self)
        self.orig = repr(self)

    def announce(self, txt):
        self.raw(txt)

    def raw(self, txt):
        Client.gotcha = True


class TestBus(unittest.TestCase):

    def test_add(self):
        clt = Client()
        self.assertTrue(clt in Bus.objs)

    def test_announce(self):
        clt = Client()
        clt.gotcha = False
        Bus.announce("test")
        self.assertTrue(Client.gotcha)

    def test_byorig(self):
        clt = Client()
        self.assertEqual(Bus.byorig(clt.orig), clt)

    def test_say(self):
        clt = Client()
        clt.gotcha = False
        Bus.say(clt.orig, "#test", "test")
        self.assertTrue(Client.gotcha)
