# This file is placed in the Public Domain.


"static tables"


import unittest


from genocide.statics import CORE


class TestStatic(unittest.TestCase):

    def test_names(self):
        self.assertTrue(CORE)
