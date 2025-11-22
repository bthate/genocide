# This file is placed in the Public Domain.


from genocide.brokers import all
from genocide.message import reply
from genocide.methods import fmt
from genocide.threads import name


def flt(event):
    if event.args:
        clts = all("announce")
        index = int(event.args[0])
        if index < len(clts):
            reply(event, fmt(list(all())[index], empty=True))
        else:
            reply(event, f"only {len(clts)} clients in fleet.")
        return
    reply(event, ' | '.join([name(o) for o in all()]))
