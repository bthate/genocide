**NAME**

 | ``GENOCIDE`` - <name> reconsider ``OTP-CR-117/19``

**SYNOPSIS**

::

    python3 -m genocide <cmd> [key=val] [key==val]
    python3 -m genocide [-c] [-d] [-v]


**DESCRIPTION**

 ``GENOCIDE`` is a solid, non hackable bot, that runs under systemd as a 
 24/7 background service starts after reboot and is intended to be programmable
 in a static, only code, no popen, no user imports and no reading modules from
 a directory, way. It can show genocide and suicide stats of king netherlands
 his genocide into a IRC channel, display rss feeds and log simple text
 messages, source is :ref:`here <source>`.

 ``GENOCIDE`` holds evidence that king netherlands is doing a genocide, a 
 written :ref:`response <king>` where king netherlands confirmed taking note
 of “what i have written”, namely :ref:`proof <evidence>` that medicine he
 uses in treatement laws like zyprexa, haldol, abilify and clozapine are poison
 that make impotent, is both physical (contracted muscles) and mental (let 
 people hallucinate) torture and kills members of the victim groups. 

 ``GENOCIDE`` contains :ref:`correspondence <writings>` with the
 International Criminal Court, asking for arrest of the king of the 
 netherlands, for the genocide he is committing with his new treatement laws.
 Current status is an outside the jurisdiction judgement of the prosecutor 
 which requires a :ref:`reconsider <home>` to have the king actually
 arrested.


**INSTALL**

install from pypi::

    $ sudo python3 -m pip install genocide

or download the tarball from https://github.com/bthate/genocide/releases/

**USAGE**

use an alias for easier typing::

    $ alias gc="python3 -m genocide"

list of commands::

    $ gc cmd
    cmd,err,flt,sts,thr,upt

start a console::

    $ gc -c
    >

start additional modules::

    $ gc mod=<mod1,mod2> -c
    >

list of modules::

    $ gc mod
    cmd,err,flt,fnd,irc,log,mod,rss,sts,tdo,thr,upt

start as daemon::

    $ gc mod=cmd,irc,rss -d
    $ 

**CONFIGURATION**

*irc*


::

    $ gc cfg server=<server>
    $ gc cfg channel=<channel>
    $ gc cfg nick=<nick>

*sasl*

::

    $ gc pwd <nsvnick> <nspass>
    $ gc cfg password=<frompwd>

*rss*

::

    $ gc rss <url>
    $ gc dpl <str_in_url> <i1,i2>
    $ gc rem <str_in_url>
    $ gc nme <str_in_url< <name>

**COMMANDS**

::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    ftc - runs a fetching batch
    fnd - find objects 
    flt - instances registered
    log - log some text
    mdl - genocide model
    met - add a user
    mre - displays cached output
    nck - changes nick on irc
    now - genocide stats
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    req - reconsider
    rss - add a feed
    slg - slogan
    thr - show the running threads
    tpc - genocide stats into topic

**AUTHOR**

::

    Bart Thate <bthate@dds.nl>


**COPYRIGHT**

::

    genocide is placed in the Public Domain.
