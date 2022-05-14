# This file is placed in the Public Domain.


import os


from setuptools import setup


mods = ["csl", "evt", "hdl", "obj", "rpt", "thr", "tms", "usr"]


def read():
    return open("README.rst", "r").read()


def uploadlist(dir):
    upl = []
    for file in os.listdir(dir):
        if not file or file.startswith('.'):
            continue
        d = dir + os.sep + file
        if os.path.isdir(d):   
            upl.extend(uploadlist(d))
        else:
            if file.endswith(".pyc") or file.startswith("__pycache"):
                continue
            upl.append(d)
    return upl


setup(
    name='genocide',
    version='67',
    url='https://github.com/bthate/genocide',
    author='Bart Thate',
    author_email='bthate67@gmail.com', 
    description="prosector. reconsider. OTP-CR-117/19.",
    long_description=read(),
    license='Public Domain',
    package_dir={"": "lib",
                 "genocide": "genocide"
                },
    py_modules=mods,
    packages=["genocide", "genocide.cmd"],
    zip_safe=True,
    include_package_data=True,
    data_files=[
                ("share/genocide", ["files/genocide.service",]),
                ("share/doc/genocide", uploadlist("docs")),
                ("share/doc/genocide/pdf", uploadlist("docs/pdf")),
                ("share/doc/genocide/_templates", uploadlist("docs/_static")),
                ("share/doc/genocide/_templates", uploadlist("docs/_templates")),
               ],
    scripts=["bin/genocide", "bin/genocided", "bin/genocidecmd", "bin/genocidectl"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
 