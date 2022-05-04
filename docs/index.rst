.. _admin:

.. raw:: html

    <br>

.. title:: OTP-CR-117/19

**NAME**

 **GENOCIDE** - Prosecutor. Reconsider. OTP-CR-117/19. 

**SYNOPSIS**

 | ``sudo genocidectl <cmd> [key=value] [key==value]``

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
 the king actually arrested, see :ref:`here <reconsider>`.

 **GENOCIDE** is also a solid, non hackable bot, that runs under systemd as a 
 24/7 background service and starts after reboot, intended to be programmable
 in a static, only code, no popen, no imports and no reading modules from a
 directory. It can show genocide and suicide stats into the channel, display rss
 feeds and log simple text messages. See the source code :ref:`here <source>`.

 **GENOCIDE** installs 52 files containing photo's and pdf's of communications
 between me, the first chamber, king and prosecutor. If you do not wish to have
 them installed a simple ``pip3 uninstall genocide`` will remove them from the
 system.  


**INSTALL**

 $ ``sudo pip3 install genocide``


**CONFIGURATION**

 **irc**

 | $ ``sudo genocidectl cfg server=<server> channel=<channel> nick=<nick>``
 |
 | (*) default channel/server is #genocide on localhost

 **sasl**

 | $ ``sudo genocidectl pwd <nickservnick> <nickservpass>``
 | $ ``sudo genocidectl cfg password=<outputfrompwd>``

 **users**

 | $ ``sudo genocidectl cfg users=True``
 | $ ``sudo genocidectl met <userhost>``

 **24/7**

 | $ ``sudo cp /usr/local/share/genocide/genocide.service /etc/systemd/system``
 | $ ``sudo systemctl enable genocide --now``


**PROGRAMMING**

 | $ ``joe genocide/hlo.py``

 ::

  from genocide.hdl import Commands


  def hlo(event):
      event.reply("hello!")


  Commands.add(hlo)


**COMMANDS**

 | ``cmd`` - shows all commands
 | ``cfg`` - shows the irc configuration, also edits the config
 | ``dlt`` - removes a user from genocide
 | ``dpl`` - sets display items for a rss feed
 | ``ftc`` - runs a rss feed fetching batch
 | ``fnd`` - allows you to display objects on the datastore, read-only json files on disk 
 | ``flt`` - shows a list of instances registered to the bus
 | ``log`` - logs some text
 | ``mdl`` - genocide model
 | ``met`` - adds a users with there irc userhost
 | ``mre`` - displays cached output, channel wise.
 | ``nck`` - changes nick on irc
 | ``now`` - show genocide stats
 | ``ops`` - tries to give you operator status (+o)
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

**FILES**

 | ``docs/ECHAabilify.png``
 | ``docs/ECHAclozapine.png``
 | ``docs/ECHAhaldol.png``
 | ``docs/ECHAzyprexa.png``
 | ``docs/OTP1.png``
 | ``docs/OTP2.png``
 | ``docs/admin.rst``
 | ``docs/bevestigd.jpg``
 | ``docs/conf.py``
 | ``docs/correspondence.rst``
 | ``docs/evidence.rst``
 | ``docs/genocide3.png``
 | ``docs/guilty.rst``
 | ``docs/index.rst``
 | ``docs/informed.jpg``
 | ``docs/kamer.png``
 | ``docs/line.png``
 | ``docs/reconsider.rst``
 | ``docs/skull3.jpg``
 | ``docs/skulllinesmall3.jpg``
 | ``docs/source.rst``
 | ``docs/_static/genocide.css``
 | ``docs/_templates/base.rst``
 | ``docs/_templates/class.rst``
 | ``docs/_templates/module.rst``
 | ``docs/pdf/EM_T04_OTP-CR-117_19.pdf``
 | ``docs/pdf/EM_T07_OTP-CR-117_19_001.pdf``
 | ``docs/pdf/Kamer.pdf``
 | ``docs/pdf/bevestigd.pdf``

**SEE ALSO**

 | ``/usr/local/share/doc/genocide``

**COPYRIGHT**

 **GENOCIDE** is placed in the Public Domain. No Copyright, No License.

**AUTHOR**

 Bart Thate - bthate67@gmail.com

.. toctree::
    :hidden:
    :glob:

    correspondence
    evidence
    guilty
    reconsider
    source
