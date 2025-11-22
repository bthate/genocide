# This file is been placed in the Public Domain.


from genocide.message import reply
from genocide.workdir import types


def lst(event):
    tps = types()
    if tps:
        reply(event, ",".join({x.split(".")[-1].lower() for x in tps}))
    else:
        reply(event, "no data yet.")
