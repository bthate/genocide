# This file is placed in the Public Domain.


from .default import Default
from .package import Mods
from .workdir import Workdir


class Config(Default):

    name = ""
    version = 0

    @staticmethod
    def configure(name, version, ignore="", local=False):
        Config.name = name
        Config.version = version
        Workdir.configure(name)
        Mods.configure(f"{name}.modules", ignore, local)


def __dir__():
    return (
        'Config',
    )
