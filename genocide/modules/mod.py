# This file is placed in the Public Domain.


from genocide.message import reply
from genocide.package import modules


def mod(event):
    reply(event, ",".join(modules()))
