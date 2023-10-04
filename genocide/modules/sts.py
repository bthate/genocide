# This file is placed in the Public Domain.
#
# pylint: disable=C0116,W0105,E0402


"status of bots"


import io
import traceback


from ..runtime import Broker


def sts(event):
    nmr = 0
    for bot in Broker.objs:
        if 'state' in dir(bot):
            event.reply(str(bot.state))
            nmr += 1
    if not nmr:
        event.reply("no status")
    if not Handler.errors:
        event.reply("no errors")
        return
    for exc in Handler.errors:
        stream = io.StringIO(
                             traceback.print_exception(
                                                       type(exc),
                                                       exc,
                                                       exc.__traceback__
                                                      )
                            )
        for line in stream.readlines():
            event.reply(line)
