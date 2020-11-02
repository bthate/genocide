# TRIPLE - 3 letter modules
#
#

__copyright__= "Public Domain"

import atexit, os

from setuptools import setup
from setuptools.command.install import install

servicetxt="""[Unit]
Description=TRIPLED - 24/7 channel daemon
After=network-online.target

[Service]
Group=triple
User=triple
StandardOutput=append:/var/log/triple/triple.log
StandardError=append:/var/log/triple/triple.log
ExecStart=/usr/local/bin/triple wd=/var/lib/triple mods=irc,rss,udp

[Install]
WantedBy=multi-user.target
"""

class Install(install):
    def __init__(self, *args, **kwargs):
        super(Install, self).__init__(*args, **kwargs)
        atexit.register(postinstall)

def skipopen(txt, skip=["already"]):
    txt += " 2>&1"
    try:
        for line in os.popen(txt).readlines():
             pass
    except Exception as ex:
        for rej in skip:
           if rej in str(ex):
               return

def postinstall():
    skipopen("mkdir /var/lib/triple")
    skipopen("mkdir /var/lib/triple/mods")
    skipopen("mkdir /var/lib/triple/store")
    skipopen("mkdir /var/log/triple")
    skipopen("touch /var/log/triple/triple.log")
    skipopen("chown -R triple:triple /var/lib/triple")
    skipopen("chown -R triple:triple /var/log/triple")
    skipopen("chmod 700 /var/lib/triple/")
    skipopen("chmod 700 /var/lib/triple/mods")
    skipopen("chmod 700 /var/lib/triple/store")
    skipopen("chmod -R 400 /var/lib/triple/mods/*.py")
    skipopen("chmod 744 /var/log/triple/")
    skipopen("groupadd triple")
    skipopen("useradd triple -g triple -d /var/lib/triple")
    writeservice()

def writeservice():
    p = "/etc/systemd/system/triple.service"
    if not os.path.exists(p):
        f = open(p, "w")
        f.write(servicetxt)
        f.close()

def mods():
    import os
    return [x[:-3] for x in os.listdir("triple") if x.endswith(".py")]

def read():
    return open("README.rst", "r").read()

setup(
    name='triple',
    version='2',
    url='https://github.com/bthate/triple',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="3 letter modules",
    long_description=read(),
    license='Public Domain',
    packages=["triple"],
    namespace_packages=["triple"],
    zip_safe=False,
    scripts=["bin/triple"],
    cmdclass={'install': Install},
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
