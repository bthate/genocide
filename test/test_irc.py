# This file is placed in the Public Domain.


"irc"


import unittest


from genocide.irc import IRC


class Test_IRC(unittest.TestCase):

    def test_irc(self):
        i = IRC()
        self.assertEqual(type(i), IRC)
