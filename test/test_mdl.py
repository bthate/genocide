# This file is placed in the Public Domain.


"model"


import unittest


from op.obj import Object
from genocide.mdl import oorzaak


class Test_Composite(unittest.TestCase):

    def test_composite(self):
        self.assertEqual(type(oorzaak), Object)
