# This file is placed in the Public Domain.


"thread"


import unittest


from gcide.spc import Thread


def test():
    pass


class TestThread(unittest.TestCase):

    def test_thread(self):
        thr = Thread(test, "test")
        self.assertEqual(type(thr), Thread)
