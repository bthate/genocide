
 *By law, with the use of poison, killing, torturing, castrating, destroying, in whole or in part, all elderly and all handicapped (Wzd), all criminals (Wfz) and all psychiatric patients (WvGGZ) here in the
 Netherlands*

NAME
####

::

 GENOCIDE - Reconsider OTP-CR-117/19


SYNOPSIS
========

::

  genocide <cmd> [key=val] 
  genocide <cmd> [key==val]
  genocide req
  genocide [-c] [-d] [-i] [-v]


DESCRIPTION
===========

:: 

 GENOCIDE contains correspondence  with the International Criminal Court, asking
 for arrest of the king of the  netherlands, for the genocide he is committing
 with his new treatement laws.  Current status is "no basis to proceed" judgement
 of the prosecutor  which requires a "basis to prosecute" to have the king
 actually arrested. The prosecutor can decide at any time to initiate a
 prosecution.

 GENOCIDE holds evidence that king netherlands is doing a genocide, a 
 written response where king netherlands confirmed taking note
 of “what i have written”, namely proof that medicine he
 uses in treatement laws like zyprexa, haldol, abilify and clozapine are poison
 that make impotent, is both physical (contracted muscles) and mental (let 
 people hallucinate) torture and kills members of the victim groups. 

 GENOCIDE is a python3 IRC bot is intended to be programmable  in a
 static, only code, no popen, no user imports and no reading modules from
 a directory, way. It can display rss feeds and log simple text
 messages.


INSTALL
=======

::

 pipx install genocide


USAGE
=====


default action is doing nothing::

 $ genocide
 $

first argument is a command::

 $ genocide cmd
 cfg,cmd,dlt,dne,dpl,fnd,log,met,mod,mre,
 nme,pwd,rem,rss,sts,tdo,thr,ver

starting a console requires an option::

 $ genocide -c
 >

list of modules::

 $ genocide mod
 bsc,err,flt,irc,log,mod,rss,shp,sts,tdo,
 thr,udp

to start the genocide as daemon::

 $ genocide -d
 $ 

add -v if you want to have verbose logging::

 $ genocide -cv
 BOT started Wed Nov 8 15:38:56 2023 CVI
 >


CONFIGURATION
=============


irc configuration is done with the cli interface
using the ``cfg`` command::

 $ genocide cfg server=<server>
 $ genocide cfg channel=<channel>
 $ genocide cfg nick=<nick>

sasl need a nickserv nick/password pair to generate
a password for sasl::

 $ genocide pwd <nsnick> <nspass>
 $ genocide cfg password=<frompwd>

rss has several configuration commands::

 $ genocide rss <url>
 $ genocide dpl <url> <item1,item2>
 $ genocide rem <url>
 $ genocide nme <url> <name>


COMMANDS
========

here is a list of the most basic commands::

 cfg - irc configuration
 cmd - commands
 dlt - remove a user
 dne - mark todo as done
 dpl - sets display items
 fnd - find objects 
 log - log some text
 met - add a user
 mre - displays cached output
 nme - display name of a feed
 pwd - sasl nickserv name/pass
 rem - removes a rss feed
 rss - add a feed
 sts - show status
 tdo - add todo item
 thr - show the running threads


SYSTEMD
=======

save the following it in /etc/systems/system/genocide.service and
replace "<user>" with the user running pipx::

 [Unit]
 Description=@KarimKhanQC reconsider OTP-CR-117/19
 Requires=network.target
 After=network.target

 [Service]
 Type=simple
 User=<user>
 Group=<user>
 WorkingDirectory=/home/<user>/.genocide
 ExecStart=/home/<user>/.local/pipx/venvs/genocide/bin/genocide -d
 RemainAfterExit=yes

 [Install]
 WantedBy=multi-user.target

then run this::

 sudo systemctl enable genocide --now

 default channel/server is #genocide on localhost


FILES
=====

::

 ~/.genocide
 ~/.local/bin/genocide
 ~/.local/pipx/venvs/genocide/


AUTHOR
======

::


 Bart Thate <bthate@dds.nl>


COPYRIGHT
=========

::

 GENOCIDE is a contribution back to society and is Public Domain.
