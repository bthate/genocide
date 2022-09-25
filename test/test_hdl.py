# This file is placed in the Public Domain.


"handler"


import unittest


from genocide.gcd import Handler


class TestHandler(unittest.TestCase):

    def testconstructor(self):
        hdl = Handler()
        self.assertEqual(type(hdl), Handler)
