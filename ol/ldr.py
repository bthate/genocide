# GENOCIDE - the king of the netherlands commits genocide
#
# OTP-CR-117/19/001 otp.informationdesk@icc-cpi.int https://genocide.rtfd.io

"module loader"

import importlib
import inspect
import ol
import pkgutil

class Loader(ol.Object):

    "holds modules table"

    #:
    table = ol.Object()

    def load(self, name):
        "load module"
        if name not in self.table:
            self.table[name] = importlib.import_module(name)
        return self.table[name]
