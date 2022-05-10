# This file is placed in the Public Domain.


from scn import scan


class Table():

    mod = {}

    @staticmethod
    def add(o):
        Table.mod[o.__name__] = o
        scan(o)

    @staticmethod
    def get(nm):
        return Table.mod.get(nm, None)
