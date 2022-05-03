.. _admin:

.. title:: admin


.. raw:: html

    <br>

admin
=====

**NAME**

 **GENOCIDE** - Prosecutor. Reconsider. OTP-CR-117/19. (:ref:`source <source>`).


**INSTALL**

 ``pip3 install genocide``


**SYNOPSIS**

 | ``genocidectl <cmd> [key=value] [key==value]``

**DESCRIPTION**

 **GENOCIDE** is a python3 program that holds evidence that the king of the
 netherlands is doing a genocide, a written response where the king of
 the netherlands confirmed taking note of “what i have written”, namely
 proof that medicine he uses in treatement laws like zyprexa, haldol,
 abilify and clozapine are poison that makes impotent, is both physical
 (contracted muscles) and mental (let people hallucinate) torture and kills
 members of the victim groups.

 **GENOCIDE** contains correspondence with the International Criminal Court, 
 asking for arrest of the king of the netherlands, for the genocide he is
 committing with his new treatement laws. Current status is an outside the
 jurisdiction judgement of the prosecutor which requires a reconsider to have
 the king actually arrested.

 **GENOCIDE** is also a solid, non hackable bot, that runs under systemd as a 
 24/7 background service and starts after reboot, intended to be programmable
 in a static, only code, no popen, no imports and no reading modules from a
 directory. It can show genocide and suicide stats into the hannel, display rss
 feeds and log simple text messages. Both feeds and logs are searchable.

 **GENOCIDE** install 97 files containing photo's of communications between
 me, the first chamber, king and prosecutor. If you do not wish to have them 
 installed a simple pip3 uninstall will remove them from the system.  


**CONFIGURATION**

configuration is done by calling the config command of the ``genocidectl``
program.

**irc**

 | ``genocidectl cfg server=<server> channel=<channel> nick=<nick>``
 |
 | (*) default channel/server is #botlib on localhost

**sasl**

 | ``genocidectl pwd <nickservnick> <nickservpass>``
 | ``genocidectl cfg password=<outputfrompwd>``

**users**

 | ``genocidectl cfg users=True``
 | ``genocidectl met <userhost>``

**RUNNING**

 to make genocide running under systemd, you need to copy it's service file
 and enable the genocide service.

 | ``cp /usr/local/share/genocide/genocide.service``
 | ``systemctl enable genocide --now``


**COMMANDS**

the bot has the following commands.

 | ``genocidectl cmd``
 | ``cfg,cmd,dlt,dpl,flt,fnd,ftc,met,nam,nck,ops,pwd,rem,rss,thr``


here is a short description of the commands.

 | ``cmd`` - shows all commands
 | ``cfg`` - shows the irc configuration, also edits the config
 | ``dlt`` - removes a user from bot
 | ``dpl`` - sets display items for a rss feed
 | ``ftc`` - runs a rss feed fetching batch
 | ``fnd`` - allows you to display objects on the datastore, read-only json files on disk 
 | ``flt`` - shows a list of bot registered to the bus
 | ``log`` - logs some text
 | ``mdl`` - genocide model
 | ``met`` - adds a users with there irc userhost
 | ``mre`` - displays cached output, channel wise.
 | ``nck`` - changes nick on irc
 | ``now`` - show genocide stats
 | ``ops`` - tries to have the bot give you operator status (+o)
 | ``pwd`` - combines a nickserv name/password into a sasl password
 | ``rem`` - removes a rss feed by matching is to its url
 | ``req`` - request to the prosecutor
 | ``rss`` - adds a feed to fetch, fetcher runs every 5 minutes
 | ``slg`` - slogan
 | ``sts`` - suidicde stats
 | ``thr`` - show the running threads
 | ``tpc`` - set genocide stats in topic
 | ``trt`` - torture definition
 | ``wsd`` - wisdom


**PROGRAMMING**

 ``git clone https://github.com/bthate/genocide``

 ``joe genocide/hlo.py``

::

 from genocide.hdl import Commands


 def hlo(event):
     event.reply("hello!")


 Commands.add(hlo)


**FILES**

 | README.rst
 | setup.py
 | bin/genocide
 | bin/genocidecmd
 | bin/genocidectl
 | bin/genocided
 | docs/ECHAabilify.png
 | docs/ECHAclozapine.png
 | docs/ECHAhaldol.png
 | docs/ECHAzyprexa.png
 | docs/OTP1.png
 | docs/OTP2.png
 | docs/admin.rst
 | docs/bevestigd.jpg
 | docs/conf.py
 | docs/correspondence.rst
 | docs/evidence.rst
 | docs/genocide.cmds.rst
 | docs/genocide.evt.rst
 | docs/genocide.hdl.rst
 | docs/genocide.irc.rst
 | docs/genocide.mdl.rst
 | docs/genocide.obj.rst
 | docs/genocide.req.rst
 | docs/genocide.rpt.rst
 | docs/genocide.rss.rst
 | docs/genocide.slg.rst
 | docs/genocide.sui.rst
 | docs/genocide.thr.rst
 | docs/genocide.trt.rst
 | docs/genocide.wsd.rst
 | docs/genocide3.png
 | docs/guilty.rst
 | docs/index.rst
 | docs/informed.jpg
 | docs/kamer.png
 | docs/line.png
 | docs/reconsider.jpg
 | docs/reconsider2.jpg
 | docs/skull3.jpg
 | docs/skulllinesmall3.jpg
 | docs/source.rst
 | docs/_static/genocide.css
 | docs/_templates/base.rst
 | docs/_templates/class.rst
 | docs/_templates/module.rst
 | docs/pdf/EM_T04_OTP-CR-117_19.pdf
 | docs/pdf/EM_T07_OTP-CR-117_19_001.pdf
 | docs/pdf/Kamer.pdf
 | docs/pdf/bevestigd.pdf
 | files/genocide.1.gz
 | files/genocide.1.md
 | files/kamer.rst
 | files/kamer1
 | files/kamer2
 | files/otp1.rst
 | files/otp2.rst
 | files/otpcr11719.rst
 | files/otpcr11719a.rst
 | genocide/__init__.py
 | genocide/cmds.py
 | genocide/evt.py
 | genocide/hdl.py
 | genocide/irc.py
 | genocide/mdl.py
 | genocide/obj.py
 | genocide/req.py
 | genocide/rpt.py
 | genocide/rss.py
 | genocide/slg.py
 | genocide/sui.py
 | genocide/thr.py
 | genocide/trt.py
 | genocide/wsd.py
 | genocide.egg-info/PKG-INFO
 | genocide.egg-info/SOURCES.txt
 | genocide.egg-info/dependency_links.txt
 | genocide.egg-info/not-zip-safe
 | genocide.egg-info/top_level.txt

**COPYRIGHT**

 **GENOCIDE** is placed in the Public Domain. No Copyright, No License.

**AUTHOR**

 Bart Thate - bthate67@gmail.com
