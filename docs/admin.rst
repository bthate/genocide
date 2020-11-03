.. _admin:

admin
#####

Welcome to GENOCIDE,

GENOCIDE is a pure python3 IRC chat bot that can run as a background daemon
for 24/7 a day presence in a IRC channel. It installs itself as a service so
you can get it restarted on reboot. You can use it to display RSS feeds, act as a
UDP to IRC gateway, program your own commands for it, have it log objects on
disk and search them and scan emails for correspondence analysis. GENOCIDE uses
a JSON in file database with a versioned readonly storage. It reconstructs
objects based on type information in the path and uses a "dump OOP and use
OP" programming library where the methods are factored out into functions
that use the object as the first argument. GENOCIDE is placed in the Public
Domain and has no COPYRIGHT or LICENSE.

it also provides information on the genocide the king of the netherlands is
doing. See https://pypi.org/project/genocide/ 

INSTALL
=======

installation is through pypi:

::

 > sudo pip3 install genocide

if you have previous versions already installed and things fail try to force reinstall:

::

 > sudo pip3 install genocide --upgrade --force-reinstall

if this also doesn't work you'll need to remove all installed previous  versions, so you can do a clean install.

you can run directly from the tarball, see https://pypi.org/project/genocide/#files

OBJECT PROGRAMMING
==================

GENOCIDE uses the TRIPLE library as object library, it provides a "move all methods to functions" like this:

::

 obj.method(*args) -> method(obj, *args) 

 e.g.

 not:

 >>> import ol
 >>> o = ol.Object()
 >>> o.set("key", "value")
 >>> o.key
 'value'

 but:

 >>> import ol
 >>> o = ol.Object()
 >>> ol.set(o, "key", "value")
 >>> o.key
 'value'

A way of programming with objects, replacing OOP., it works because the
object library is 2 characters long and using the, now generic, method is
not too much typing.

it's a way of programming with objects, replacing OOP. Not object-oriented programming, but object programming. If you are used to functional programming you'll like it (or not) ;]

TRIPLE has the following modules:

::

    triple 	- object programming library
    triple.bus	- announce
   triple.cfg	- config
    triple.csl	- console
    triple.dbs	- databases
    triple.evt	- event
    triple.hdl	- handler
    triple.int	- introspection
    triple.krn	- kernel
    triple.prs 	- parser
    triple.tms	- times
    triple.trm	- terminal
    triple.tsk	- tasks
    triple.utl	- utilities

MODULES
=======

GENOCIDE uses mods as the namespace to distribute modules for GENOCIDE:

::

   triple.cmd	- command
   triple.ent	- entry
   triple.fnd	- find
   triple.hlp	- help
   triple.irc	- irc 
   triple.mbx	- mail
   triple.req	- request
   triple.rss	- rich site syndicate
   triple.sui	- suicide
   triple.trt	- torture
   triple.udp	- UDP to IRC
   triple.wsd	- wisdom


USAGE
=====

GENOCIDE has it's own CLI, you can run it by giving the genocide command on the prompt, it will return with no response:

:: 

 $ sudo genocide
 $ 

you can use genocide <cmd> to run a command directly, use the cmd command to see a list of commands:

::

 $ sudo genocide cmd
 cfg,cmd,cor,dne,dpl,fed,fnd,ftc,log,mbx,rem,req,rss,sts,tdo,trt,tsk,upt,ver,wsd

GENOCIDE also has it's own shell, use genocide -s to start a genocide shell:

::

  $ sudo genocide -s
  > cmd
  cfg,cmd,cor,dne,dpl,fed,fnd,ftc,log,mbx,rem,req,rss,sts,tdo,trt,tsk,upt,ver,wsd


IRC
===

configuration is done with the cfg command:

::

 $ sudo genocide cfg
 channel=#genocide nick=genocide port=6667 server=localhost

you can use setters to edit fields in a configuration:

::

 $ genocide cfg server=irc.freenode.net channel=\#genocude nick=genocide
 channel=#genocide nick=genocide port=6667 server=irc.freenode.net

to have the irc bot started use the mods=irc option at start:

::

 $ sudo genocide mods=irc

RSS
===

GENOCIDE provides with the use of feedparser the possibility to server rss
feeds in your channel. GENOCIDE itself doesn't depend, you need to install
python3-feedparser first:

::

 $ sudo apt install python3-feedparser
 $

adding rss to mods= will load the rss module and start it's poller.

::

 $ sudo genocide mods=irc,rss

to add an url use the rss command with an url:

::

 $ sudo genocide rss https://github.com/bthate/botlib/commits/master.atom
 ok 1

run the rss command to see what urls are registered:

::

 $ sudo genocide fnd rss
 0 https://github.com/bthate/botlib/commits/master.atom

the ftc (fetch) command can be used to poll the added feeds:

::

 $ sudo genocide ftc
 fetched 20

UDP
===

GENOCIDE also has the possibility to serve as a UDP to IRC relay where you
can send UDP packages to the bot and have txt displayed on the channel.

use the 'genocide udp' command to send text via the bot to the channel on the irc server:

::

 $ tail -f /var/log/syslog | genocide udp

output to the IRC channel can be done with the use python3 code to send a UDP packet 
to genocide, it's unencrypted txt send to the bot and display on the joined channels.

to send a udp packet to genocide in python3:

::

 import socket

 def toudp(host=localhost, port=5500, txt=""):
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     sock.sendto(bytes(txt.strip(), "utf-8"), host, port)


SERVICE
=======

If you want to run GENOCIDE as a 24/7 service in your channel, you can run
the genocide-install program, it will install a service file in 
/etc/systemd/system/genocide.service and create the necesarry directories in
/var/lib/genocide.

::

 $ sudo genocide-install

after installing the service file, configure genocide to connect to irc:

::

 $ sudo genocide cfg server=irc.freenode.net channel=#dunkbots nick=genocide2

then start the genocide service:

::

 $ sudo service genocide stop
 $ sudo service genocide start

check if it's running ok with:

::

 $ sudo systemctl status genocide


genocide should join your configured channel or #genocide as a default.

if you don't want genocide to startup at boot, you can disable it:

::

 $ sudo systemctl disable genocide

or remove the service file:

::

 $ sudo rm /etc/systemd/system/genocide.service

CONTACT
=======

"hope you enjoy my contribution back to society."

you can contact me on IRC/freenode/#dunkbots or email me at bthate@dds.nl

| Bart Thate (bthate@dds.nl, thatebart@gmail.com)
| botfather on #dunkbots irc.freenode.net
