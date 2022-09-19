# This file is placed in the Public Domain.
# pylint: disable=C0112,C0103,C0114,C0115,C0116


"working directory"


import os


def __dir__():
    return (
            "Wd",
           )


from cid.utl import cdir


class Wd:

    "class level working directory pointer."

    workdir = ".genocide"

    @staticmethod
    def get():
        "return working directory."
        return Wd.workdir

    @staticmethod
    def getpath(path):
        "return path with the ``store`` directory."
        return os.path.join(Wd.workdir, "store", path)

    @staticmethod
    def set(path):
        "set working directory."
        Wd.workdir = path

    @staticmethod
    def storedir():
        "return the ``store`` path in the working directory."
        sdr =  os.path.join(Wd.workdir, "store", '')
        if not os.path.exists(sdr):
            cdir(sdr)
        return sdr

    @staticmethod
    def types(name=None):
        "return stored types."
        sdr = Wd.storedir()
        res = []
        for fnm in os.listdir(sdr):
            if name and name.lower() not in fnm.split(".")[-1].lower():
                continue
            if fnm not in res:
                res.append(fnm)
        return res
