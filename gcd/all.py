# This file is placed in the Public Domain

"all modules"

from gcd.krn import Kernel

import gcd.bus
import gcd.cfg
import gcd.clk
import gcd.clt
import gcd.cmd
import gcd.cms
import gcd.dbs
import gcd.dft
import gcd.evt
import gcd.hdl
import gcd.irc
import gcd.krn
import gcd.lst
import gcd.obj
import gcd.opt
import gcd.prs
import gcd.thr

Kernel.addmod(gcd.bus)
Kernel.addmod(gcd.cfg)
Kernel.addmod(gcd.clk)
Kernel.addmod(gcd.clt)
Kernel.addmod(gcd.cmd)
Kernel.addmod(gcd.cms)
Kernel.addmod(gcd.dft)
Kernel.addmod(gcd.evt)
Kernel.addmod(gcd.hdl)
Kernel.addmod(gcd.irc)
Kernel.addmod(gcd.krn)
Kernel.addmod(gcd.lst)
Kernel.addmod(gcd.obj)
Kernel.addmod(gcd.opt)
Kernel.addmod(gcd.prs)
Kernel.addmod(gcd.thr)
