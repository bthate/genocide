# OLIB - object library
#
#

"""
specification

classes
=======

.. autoclass:: ol.bus.Bus
    :noindex:

.. autoclass:: ol.Default
    :noindex:

.. autoclass:: ol.csl.Console
    :noindex:

.. autoclass:: ol.evt.Event
    :noindex:

.. autoclass:: ol.hdl.Handler
    :noindex:

.. autoclass:: ol.krn.Kernel
    :noindex:

.. autoclass:: ol.ldr.Loader
    :noindex:

.. autoclass:: ol.Object
    :noindex:

.. autoclass:: ol.Ol
    :noindex:

.. autoclass:: ol.tsk.Task
    :noindex:

functions
=========

.. autofunction:: ol.krn.boot
    :noindex:

.. autofunction:: ol.bus.bus
    :noindex:

.. autofunction:: ol.utl.cdir
    :noindex:


.. autofunction:: ol.krn.cmd
    :noindex:

.. autofunction:: ol.trm.execute
    :noindex:

.. autofunction:: ol.krn.get_kernel
    :noindex:

.. autofunction:: ol.tsk.launch
    :noindex:

.. autofunction:: ol.prs.parse_cli
    :noindex:

.. autofunction:: ol.utl.privileges
    :noindex:

.. autofunction:: ol.utl.root
    :noindex:

.. autofunction:: ol.krn.scandir
    :noindex:

"""

import ol
import os
import pwd
import sys
import time

from ol.bus import Bus, bus
from ol.csl import Console
from ol.evt import Event
from ol.hdl import Handler
from ol.krn import Kernel, boot, cmd, get_kernel, scandir
from ol.ldr import Loader
from ol.prs import parse, parse_cli
from ol.tsk import launch
from ol.trm import execute
from ol.utl import cdir, privileges, root
