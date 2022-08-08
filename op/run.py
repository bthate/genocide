# This file is placed in the Public Domain.


"runtime"


import inspect
import os
import sys
import termios


from op.obj import Cfg, Class, Object, get, register
from op.hdl import Bus, Callbacks, Command, Event, Handler


def __dir__():
    return (
        "Table",
        "CLI",
        "Commands",
        "dispatch",
        "parse_cli"
    )


class Table():

    mod = {}

    @staticmethod
    def add(obj):
        Table.mod[obj.__name__] = obj

    @staticmethod
    def exec(cmd):
        for mod in Table.mod.values():
            func = getattr(mod, cmd, None)
            if func:
                func()

    @staticmethod
    def get(name):
        return Table.mod.get(name, None)

    @staticmethod
    def scan(mns=None):
        for mod in Table.mod.values():
            if mns and mod.__name__ not in mns:
                continue
            for _k, obj in inspect.getmembers(mod, inspect.isfunction):
                if "event" in obj.__code__.co_varnames:
                    Commands.add(obj)
            for _k, clz in inspect.getmembers(mod, inspect.isclass):
                Class.add(clz)


class Commands(Object):

    cmd = Object()

    @staticmethod
    def add(cmd):
        register(Commands.cmd, cmd.__name__, cmd)

    @staticmethod
    def get(cmd):
        return get(Commands.cmd, cmd)


    @staticmethod
    def remove(cmd):
        del Commands.cmd[cmd]


class CLI(Handler):

    def announce(self, txt):
        self.raw(txt)

    def cmd(self, txt):
        cmd = Command()
        cmd.channel = ""
        cmd.orig = repr(self)
        cmd.txt = txt
        self.handle(cmd)
        cmd.wait()

    def raw(self, txt):
        print(txt)


class Console(CLI):

    def handle(self, e):
        Handler.handle(e)
        e.wait()

    def poll(self):
        e = Command()
        e.channel = ""
        e.cmd = ""
        e.txt = input("> ")
        e.orig = repr(self)
        if e.txt:
            e.cmd = e.txt.split()[0]
        return e


def dispatch(event):
    event.parse()
    func = Commands.get(event.cmd)
    if func:
        func(event)
        event.show()
    event.ready()


def parse_cli(txt):
    event = Event()
    event.parse(txt)
    return event


Callbacks.add("command", dispatch)
