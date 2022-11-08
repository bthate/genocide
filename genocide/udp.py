# This file is placed in the Public Domain.


"udp to irc relay"


## imports

import socket
import time


from .hdl import Bus
from .obj import Class, Object, last
from .thr import launch


## defines

def __dir__():
    return (
            "Cfg",
            "UDP",
            "init",
           )


def init():
    udp = UDP()
    udp.start()
    return udp


## classes


class Cfg(Object):

    def __init__(self):
        super().__init__()
        self.host = "localhost"
        self.port = 5500


Class.add(Cfg)


class UDP(Object):

    def __init__(self):
        super().__init__()
        self.stopped = False
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self._sock.setblocking(1)
        self._starttime = time.time()
        self.cfg = Cfg()

    @staticmethod
    def output(txt):
        Bus.announce(txt.replace("\00", ""))

    def server(self):
        try:
            self._sock.bind((self.cfg.host, self.cfg.port))
        except socket.gaierror:
            return
        while not self.stopped:
            (txt, _addr) = self._sock.recvfrom(64000)
            if self.stopped:
                break
            data = str(txt.rstrip(), "utf-8")
            if not data:
                break
            self.output(data)

    def exit(self):
        self.stopped = True
        self._sock.settimeout(0.01)
        self._sock.sendto(bytes("exit", "utf-8"), (self.cfg.host, self.cfg.port))

    def start(self):
        last(self.cfg)
        launch(self.server)
