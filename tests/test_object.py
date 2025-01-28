# This file is placed in the Public Domain.


"objects"


import unittest


from genocide.objects import Object, items, keys, update, values


import genocide


VALIDJSON = '{"test": "bla"}'


attrs1 = (
    'Object',
    'Obj',
    'construct',
    'dumps',
    'fqn',
    'items',
    'update',
    'keys',
    'loads',
    'values'
)


attrs2 = (
    '__doc__',
    '__lt__',
    '__init__',
    '__setattr__',
    '__ne__',
    '__delattr__',
    '__eq__',
    '__dir__',
    '__new__',
    '__iter__',
    '__reduce__',
    '__class__',
    '__module__',
    '__gt__',
    '__str__',
    '__init_subclass__',
    '__reduce_ex__',
    '__dict__',
    '__subclasshook__',
    '__le__',
    '__contains__',
    '__weakref__',
    '__ge__',
    '__sizeof__',
    '__getattribute__',
    '__format__',
    '__len__',
    '__getstate__',
    '__repr__',
    '__hash__'
)


OBJECT  = Object()
PACKAGE = genocide.objects


class TestObject(unittest.TestCase):

    """ TestObject """

    def test_attributes(self):
        """ attribute test. """
        okd = True
        for meth in attrs2:
            print(meth)
            mth = getattr(OBJECT, meth, None)
            if mth is None:
                okd = meth
        self.assertTrue(okd)

    def test_constructor(self):
        """ constructor test. """
        obj = Object()
        self.assertTrue(type(obj), Object)

    def test_class(self):
        """ class tests. """
        obj = Object()
        clz = obj.__class__()
        self.assertTrue("Object" in str(type(clz)))

    def test_delattr(self):
        """ detelete attribute test. """
        obj = Object()
        obj.key = "value"
        del obj.key
        self.assertTrue("key" not in dir(obj))

    def test_dict(self):
        """ dictionary test. """
        obj = Object()
        self.assertEqual(obj.__dict__, {})

    def test_getattribute(self):
        """ getattributes test. """
        obj = Object()
        obj.key = "value"
        self.assertEqual(getattr(obj, "key"), "value")

    def test_getattr(self):
        """ getattr test. """
        obj = Object()
        obj.key = "value"
        self.assertEqual(getattr(obj, "key"), "value")

    def test_hash(self):
        """ hash test. """
        obj = Object()
        hsj = hash(obj)
        self.assertTrue(isinstance(hsj, int))

    def test_init(self):
        """ init test. """
        obj = Object()
        self.assertTrue(type(Object.__init__(obj)), Object)

    def test_items(self):
        """ items test. """
        obj = Object()
        obj.key = "value"
        self.assertEqual(
            list(items(obj)),
            [
                ("key", "value"),
            ],
        )

    def test_keys(self):
        """ keys test. """
        obj = Object()
        obj.key = "value"
        self.assertEqual(
            list(keys(obj)),
            [
                "key",
            ],
        )

    def test_methods(self):
        """ methods test. """
        okd = True
        for attr in attrs1:
            att = getattr(PACKAGE, attr, None)
            if not att:
                okd = attr
                break
        self.assertTrue(okd)

    def test_module(self):
        """ module test. """
        self.assertEqual(Object().__module__, "genocide.objects")

    def test_register(self):
        """ register test. """
        obj = Object()
        setattr(obj, "key", "value")
        self.assertEqual(obj.key, "value")

    def test_repr(self):
        """ repr test. """
        self.assertTrue(repr(update(Object(), {"key": "value"})), {"key": "value"})

    def test_setattr(self):
        """ setattr test. """
        obj = Object()
        setattr(obj, "key", "value")
        self.assertTrue(obj.key, "value")

    def test_update(self):
        """ update test. """
        obj = Object()
        obj.key = "value"
        oobj = Object()
        update(oobj, obj)
        self.assertTrue(oobj.key, "value")

    def test_values(self):
        """ values test. """
        obj = Object()
        obj.key = "value"
        self.assertEqual(
            list(values(obj)),
            [
                "value",
            ],
        )
