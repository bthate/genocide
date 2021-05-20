"all modules"

from gcd.krn import Kernel

import genocide.adm
import genocide.fnd
import genocide.log
import genocide.rss
import genocide.slg
import genocide.tdo
import genocide.udp

Kernel.addmod(genocide.adm)
Kernel.addmod(genocide.fnd)
Kernel.addmod(genocide.log)
Kernel.addmod(genocide.rss)
Kernel.addmod(genocide.slg)
Kernel.addmod(genocide.tdo)
Kernel.addmod(genocide.udp)
