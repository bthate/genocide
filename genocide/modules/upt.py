# This file is placed in the Public Domain.


import time


from genocide.message import reply
from genocide.utility import elapsed


STARTTIME = time.time()


def upt(event):
    reply(event, elapsed(time.time()-STARTTIME))
