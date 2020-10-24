# OLIB - object library
#
#

"module loader"

import importlib
import inspect
import ol
import pkgutil

class Loader(ol.Object):

    "holds modules table"

    table = ol.Object()

    def load(self, name):
        if name not in self.table:
            self.table[name] = importlib.import_module(name)
        return self.table[name]
