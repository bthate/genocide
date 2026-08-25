# This file is placed in the Public Domain.


"show path to website"


import os


from genocide.defines import Main


a = os.path.abspath
d = os.path.dirname
e = os.path.exists
j = os.path.join


def pth(event):
    "create and show path to website."
    if Main.sets.docs:
        path = j(a(Main.sets.docs), "index.html")
    else:
        path = j(d(d(__file__)), "numbers", "index.html")
    if e(path):
        event.reply(f"file://{path}")
    else:
        event.reply("no index.html")
