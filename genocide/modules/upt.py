# This file is placed in the Public Domain.


"show uptime"


import time


from genocide.utility import Time


STARTTIME = time.time()


def upt(event):
    event.reply(Time.elapsed(time.time()-STARTTIME))
