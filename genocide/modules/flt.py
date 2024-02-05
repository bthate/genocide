# This file is placed in the Public Domain.
#
# pylint: disable=C,R


"fleet"


from .. import Broker, name, values


def flt(event):
    try:
        event.reply(values(Broker.objs)[int(event.args[0])])
    except (IndexError, ValueError):
        event.reply(",".join([name(x).split(".")[-1] for x in values(Broker.objs)]))
