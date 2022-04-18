# This file is placed in the Public Domain.


"object all"


def __dir__():
    return (
        "obj",
        "obs",
        "ocb",
        "ocl",
        "odb",
        "oev",
        "ofn",
        "ohd",
        "ojs",
        "oqu",
        "orp",
        "otb",
        "oth",
        "otm"
    )


from otb import Table

import obj
import obs
import ocb
import ocl
import odb
import oev
import ofn
import ohd
import ojs
import opr
import oqu
import orp
import otb
import oth
import otm


l = globals()

for mn in __dir__():
    md = l.get(mn)
    if md:
        Table.add(md)
