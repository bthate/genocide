#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

def read():
    return open("README", "r").read()

setup(
    name='genocide',
    version='1',
    url='https://bitbucket.org/bthate/genocide',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="OTP-CR-117/19/001 - otp.informationdesk@icc-cpi.int - the king of the netherlands commits genocide - https://genocide.rtfd.io",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license='Public Domain',
    zip_safe=False,
    scripts=["bin/gc"],
    packages=["genocide", "bmod", "bot", "ol"],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
