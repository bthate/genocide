# This file is placed in the Public Domain.


"database"


import unittest


from cide.spc import Db


class TestDbs(unittest.TestCase):

    def test_constructor(self):
        dbs = Db()
        self.assertEqual(type(dbs), Db)
