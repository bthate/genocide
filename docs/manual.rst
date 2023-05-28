.. _manual:

.. title:: Manual


.. raw:: html

     <br><br>


**NAME**

 | **GENOCIDE** - Reconsider ``OTP-CR-117/19``


**SYNOPSIS**

::

    python3 -m genocide <cmd> [key=val] 
    python3 -m genocide <cmd> [key==val]
    python3 -m genocide [-c] [-d] [-v]


**DESCRIPTION**


 **GENOCIDE** is a python3 IRC bot is intended to be programmable  in a
 static, only code, no popen, no user imports and no reading modules from
 a directory, way. It can show genocide and suicide stats of king netherlands
 his genocide into a IRC channel, display rss feeds and log simple text
 messages, source is :ref:`here <source>`.

 **GENOCIDE** holds evidence that king netherlands is doing a genocide, a 
 written :ref:`response <king>` where king netherlands confirmed taking note
 of “what i have written”, namely :ref:`proof <evidence>` that medicine he
 uses in treatement laws like zyprexa, haldol, abilify and clozapine are poison
 that make impotent, is both physical (contracted muscles) and mental (let 
 people hallucinate) torture and kills members of the victim groups. 

 **GENOCIDE** contains :ref:`correspondence <writings>` with the
 International Criminal Court, asking for arrest of the king of the 
 netherlands, for the genocide he is committing with his new treatement laws.
 Current status is an outside the jurisdiction judgement of the prosecutor 
 which requires a :ref:`reconsider <home>` to have the king actually
 arrested.


**INSTALL**


::

 $ sudo python3 -m pip install genocide


**USAGE**


 use an alias for easier typing::

    $ alias gcd="python3 -m genocide"

 list of commands::

    $ gcd cmd
    cmd,err,flt,sts,thr,upt

 start a console::

    $ gcd -c
    >

 start additional modules::

    $ gcd mod=<mod1,mod2> -c
    >

 list of modules::

    $ gcd mod
    cmd,err,flt,fnd,irc,log,mdl,mod,req,
    rss,slg,sts,tdo,thr,upt,ver

 to start irc, add mod=irc when starting::

     $ gcd mod=irc -c

 to start rss, also add mod=rss when starting::

     $ gcd mod=irc,rss -c

 start as daemon::

    $ gcd mod=irc,rss -d
    $ 


**CONFIGURATION**


 *irc*

 ::

    $ gcd cfg server=<server>
    $ gcd cfg channel=<channel>
    $ gcd cfg nick=<nick>

 *sasl*

 ::

    $ gcd pwd <nsvnick> <nspass>
    $ gcd cfg password=<frompwd>

 *rss*

 ::

    $ gcd rss <url>
    $ gcd dpl <str_in_url> <item1,item2>
    $ gcd rem <str_in_url>
    $ gcd nme <str_in_url< <name>


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


**FILES**


 | ``/usr/local/share/doc/genocide/*``
 | ``/usr/local/genocide/``


**AUTHOR**


 | Bart Thate <bthate@dds.nl>


**COPYRIGHT**


 | **GENOCIDE** is placed in the Public Domain.
