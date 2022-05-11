# This file is placed in the Public Domain.


import genocide


def __dir__():
    return (
        "cmds",
        "mdl",
        "req",
        "slg",
        "sui",
        "trt",
        "wsd",
    )


from tbl import Table


from genocide import mdl as mdl
from genocide import req as req
from genocide import slg as slg
from genocide import sui as sui
from genocide import trt as trt
from genocide import wsd as wsd
from genocide import cmds as cmds


for mn in __dir__():
    md = getattr(locals(), mn, None)
    if md:
        Table.add(md)
