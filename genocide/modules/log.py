# This file is placed in the Public Domain.


import time


from genocide.objects import Object
from genocide.message import reply
from genocide.persist import find, fntime, write
from genocide.utility import elapsed


class Log(Object):

    def __init__(self):
        super().__init__()
        self.txt = ''


def log(event):
    if not event.rest:
        nmr = 0
        for fnm, obj in find('log', event.gets):
            lap = elapsed(time.time() - fntime(fnm))
            reply(event, f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            reply(event, 'no log')
        return
    obj = Log()
    obj.txt = event.rest
    write(obj)
    reply(event, "ok")
