# This file is placed in the Public Domain.


from genocide.brokers import get as bget
from genocide.message import reply


def sil(event):
    bot = bget(event.orig)
    bot.silent = True
    reply(event, "ok")


def lou(event):
    bot = bget(event.orig)
    bot.silent = False
    reply(event, "ok")
