# This file is placed in the Public Domain.


import time


from genocide.message import reply
from genocide.methods import fmt
from genocide.persist import find, fntime
from genocide.utility import elapsed
from genocide.workdir import types


def fnd(event):
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in types()])
        if res:
            reply(event, ",".join(res))
        else:
            reply(event, "no data yet.")
        return
    otype = event.args[0]
    nmr = 0
    for fnm, obj in list(find(otype, event.gets)):
        reply(event, f"{nmr} {fmt(obj)} {elapsed(time.time()-fntime(fnm))}")
        nmr += 1
    if not nmr:
        reply(event, "no result")
