# This file is placed in the Public Domain.


"fields"


from genocide.message import reply
from genocide.persist import attrs
from genocide.workdir import types


def atr(event):
    if not event.rest:
        res = sorted([x.split('.')[-1].lower() for x in types()])
        if res:
            reply(event, ",".join(res))
        else:
            reply(event, "no types")
        return
    items = attrs(event.args[0])
    if not items:
        reply(event, "no fields")
    else:
        reply(event, ",".join(items))
