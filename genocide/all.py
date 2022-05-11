# This file is placed in the Public Domain.


def __dir__():
    return (
        "mdl",
        "req",
        "slg",
        "sui",
        "trt",
        "wsd",
        "cmds"
    )


from tbl import Table


from genocide import mdl
from genocide import req
from genocide import slg
from genocide import sui
from genocide import trt
from genocide import wsd
from genocide import cmds


for mn in __dir__():
    md = getattr(locals(), mn, None)
    if md:
        Table.add(md)
