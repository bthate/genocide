# This file is placed in the Public Domain.


import genocide.bsc as bsc
import genocide.mdl as mdl
import genocide.irc as irc
import genocide.rss as rss


from .hdl import Table


Table.add(bsc)
Table.add(mdl)
Table.add(irc)
Table.add(rss)
