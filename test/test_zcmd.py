# This file is placed in the Public Domain.


"command"


import unittest


from op.evt import Command
from op.obj import Object, get
from op.run import CLI, Commands, Config


evts = []
skip = ["cfg",]


param = Object()
param.cmd = [""]
param.cfg = ["nick=genocide", "server=localhost", "port=6699"]
param.fnd = ["log", "log txt==test", "config", "config name=genocide", "config server==localhost"]
param.flt = ["0", ""]
param.log = ["test1", "test2"]
param.mre = [""]
param.thr = [""]


class CLI(CLI):

    def raw(self, txt):
        if Config.verbose:
            print(txt)


c = CLI()
c.start()


def consume(events):
    fixed = []
    res = []
    for e in events:
        e.wait()
        fixed.append(e)
    for f in fixed:
        try:
            events.remove(f)
        except ValueError:
            continue
    return res



class Test_Commands(unittest.TestCase):

    def test_commands(self):
        cmds = sorted(Commands.cmd)
        for cmd in cmds:
            print(cmd)
            if cmd in skip:
                continue
            for ex in get(param, cmd, ""):
                e = Command()
                e.channel = "#genocide"
                e.orig = repr(c)
                txt = cmd + " " + ex
                e.txt = txt.strip()
                c.handle(e)
                evts.append(e)
        consume(evts)
        self.assertTrue(not evts)
