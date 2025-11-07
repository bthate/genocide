# This file is placed in the Public Domain.


"uptime"


import time


from genocide.runtime import STARTTIME
from genocide.utility import elapsed


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
