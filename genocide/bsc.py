# This file is placed in the Public Domain.


"command"


from hx.cmd import Commands


def __dir__():
    return (
        "cmd",
    )


def reg():
    Commands.add(cmd)


def rem():
    Commands.remove(cmd)


def cmd(event):
    event.reply(",".join(sorted(Commands.cmd)))
