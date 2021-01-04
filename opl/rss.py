# OPL - object progamming library  (rss.py)
#
# this file is placed in the public domain

"rich site syndicate (rss)"

# imports

import opl
import urllib

from urllib.error import HTTPError, URLError

# defines

def __dir__():
    return ("Cfg", "Rss", "Feed", "Fetcher", "init")

try:
    import feedparser
    gotparser = True
except ModuleNotFoundError:
    gotparser = False

def init(hdl):
    "start a rss poller"
    f = Fetcher()
    return opl.thr.launch(f.start)

# classes

class Cfg(opl.Cfg):

    "rss configuration"

    def __init__(self):
        super().__init__()
        self.dosave = True

class Feed(opl.Default):

    "feed item"

class Rss(opl.Object):

    "rss feed url"

    def __init__(self):
        super().__init__()
        self.rss = ""

class Seen(opl.Object):

    "all urls seen"

    def __init__(self):
        super().__init__()
        self.urls = []

class Fetcher(opl.Object):

    "rss feed poller"

    cfg = Cfg()
    seen = Seen()

    def display(self, o):
        "display a rss feed item"
        result = ""
        dl = []
        try:
            dl = o.display_list.split(",")
        except AttributeError:
            pass
        if not dl:
            dl = self.cfg.display_list.split(",")
        if not dl or not dl[0]:
            dl = ["title", "link"]
        for key in dl:
            if not key:
                continue
            data = opl.get(o, key, None)
            if not data:
                continue
            if key == "link" and self.cfg.tinyurl:
                datatmp = opl.utl.get_tinyurl(data)
                if datatmp:
                    data = datatmp[0]
            data = data.replace("\n", " ")
            data = opl.utl.strip_html(data.rstrip())
            data = opl.utl.unescape(data)
            result += data.rstrip()
            result += " - "
        return result[:-2].rstrip()

    def fetch(self, rssobj):
        "rss feed"
        counter = 0
        objs = []
        if not rssobj.rss:
            return 0
        for o in reversed(list(get_feed(rssobj.rss))):
            if not o:
                continue
            f = Feed()
            opl.update(f, rssobj)
            opl.update(f, opl.O(o))
            u = urllib.parse.urlparse(f.link)
            if u.path and not u.path == "/":
                url = "%s://%s/%s" % (u.scheme, u.netloc, u.path)
            else:
                url = f.link
            if url in Fetcher.seen.urls:
                continue
            Fetcher.seen.urls.append(url)
            counter += 1
            objs.append(f)
            if self.cfg.dosave:
                opl.save(f)
        if objs:
            opl.save(Fetcher.seen)
        for o in objs:
            txt = self.display(o)
            opl.hdl.Bus.announce(txt)
        return counter

    def run(self):
        "all feeds"
        thrs = []
        for fn, o in opl.dbs.all("opl.rss.Rss"):
            thrs.append(opl.thr.launch(self.fetch, o))
        return thrs

    def start(self, repeat=True):
        "rss poller"
        opl.dbs.last(Fetcher.cfg)
        opl.dbs.last(Fetcher.seen)
        if repeat:
            repeater = opl.clk.Repeater(300.0, self.run)
            repeater.start()

    def stop(self):
        "rss poller"
        opl.save(self.seen)

# functions

def get_feed(url):
    "feed"
    if opl.debug:
        return [opl.Object(), opl.Object()]
    try:
        result = opl.utl.get_url(url)
    except (HTTPError, URLError):
        return [opl.Object(), opl.Object()]
    if gotparser:
        result = feedparser.parse(result.data)
        if "entries" in result:
            for entry in result["entries"]:
                yield entry
    else:
        return [opl.Object(), opl.Object()]
