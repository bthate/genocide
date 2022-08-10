# This file is placed in the Public Domain.


"find"


import time


from .obj import Db, find, fntime, printable
from .tmr import elapsed


def fnd(event):
    if not event.args:
        dbs = Db()
        res = ",".join(
            sorted({x.split(".")[-1].lower() for x in dbs.types()}))
        if res:
            event.reply(res)
        else:
            event.reply("no types yet.")
    else:
        bot = event.bot()
        otype = event.args[0]
        res = list(find(otype, event.gets))
        if bot.cache:
            if len(res) > 3:
                bot.extend(event.channel, [x[1].txt for x in res])
                bot.say(event.channel, "%s left in cache, use !mre to show more" % bot.cache.size())
        else:
            _nr = 0
            for _fn, obj in res:
                txt = "%s %s %s" % (
                                    str(_nr),
                                    printable(obj,event.sets.keys, event.toskip),
                                    elapsed(time.time()-fntime(_fn))
                                   )
                _nr += 1
                event.reply(txt)
            if not _nr:
                event.reply("no result")
