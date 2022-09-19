# This file is placed in the Public Domain.
# pylint: disable=C0114,C0115,C0116


"working directory"


import os


from cide.utl import cdir


def __dir__():
    return (
            "Wd",
           )


class Wd:

    workdir = ".genocide"

    @staticmethod
    def get():
        return Wd.workdir

    @staticmethod
    def getpath(path):
        return os.path.join(Wd.workdir, "store", path)

    @staticmethod
    def set(path):
        Wd.workdir = path

    @staticmethod
    def storedir():
        sdr =  os.path.join(Wd.workdir, "store", '')
        if not os.path.exists(sdr):
            cdir(sdr)
        return sdr

    @staticmethod
    def types(name=None):
        sdr = Wd.storedir()
        res = []
        for fnm in os.listdir(sdr):
            if name and name.lower() not in fnm.split(".")[-1].lower():
                continue
            if fnm not in res:
                res.append(fnm)
        return res