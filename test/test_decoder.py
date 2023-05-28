# This file is placed in the Public Domain.


import os
import sys
import unittest


sys.path.insert(0, os.getcwd())


from genocide.decoder import loads
from genocide.encoder import dumps
from genocide.objects import Object


class TestDecoder(unittest.TestCase):

    def test_loads(self):
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")

    def test_doctest(self):
        self.assertTrue(__doc__ is None)