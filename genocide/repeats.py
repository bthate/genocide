# This file is placed in the Public Domain.


from .clocked import Timer
from .runtime import launch
from .threads import Thread


def __dir__():
    return (
            'Repeater',
           )


class Repeater(Timer):

    def run(self) -> Thread:
        thr = launch(self.start)
        super().run()
        return thr
