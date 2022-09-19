# This file is placed in the Public Domain.
# pylint: disable=C0114,C0115,R0903


"config"


from cid.dft import Default


def __dir__():
    return (
            "Config",
           )


class Config(Default):

    pass
