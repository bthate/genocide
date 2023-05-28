# This file is placed in the Public Domain.


import os
import sys
import unittest


sys.path.insert(0, "..")


from genocide.encoder import dumps
from genocide.objects import Object


VALIDJSON = '{"test": "bla"}'


class TestEncoder(unittest.TestCase):


    def test_dumps(self):
        obj = Object()
        obj.test = "bla"
        self.assertEqual(dumps(obj), VALIDJSON)