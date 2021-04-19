# This file is placed in the Public Domain.

from .obj import Default, Object

class Names(Object):

    names = Default({
                 'bus': ['op.bus.Bus'],
                 'cfg': [   'op.obj.Cfg',
                            'op.krn.Cfg',
                            'op.rss.Cfg',
                            'op.udp.Cfg',
                            'op.irc.Cfg'],
                 'client': ['op.krn.Client', 'op.hdl.Client'],
                 'command': ['op.evt.Command'],
                 'dcc': ['op.irc.DCC'],
                 'default': ['op.obj.Default'],
                 'email': ['op.mbx.Email'],
                 'enoclass': ['op.err.ENOCLASS'],
                 'enofilename': ['op.err.ENOFILENAME'],
                 'enomore': ['op.err.ENOMORE'],
                 'enotimplemented': ['op.err.ENOTIMPLEMENTED'],
                 'enotxt': ['op.err.ENOTXT'],
                 'enouser': ['op.err.ENOUSER'],
                 'event': ['op.evt.Event', 'op.irc.Event'],
                 'feed': ['op.rss.Feed'],
                 'fetcher': ['op.rss.Fetcher'],
                 'getter': ['op.prs.Getter'],
                 'handler': ['op.hdl.Handler'],
                 'httperror': ['urllib.error.HTTPError'],
                 'irc': ['op.irc.IRC'],
                 'kernel': ['op.krn.Kernel'],
                 'loader': ['op.ldr.Loader'],
                 'log': ['op.log.Log'],
                 'names': ['op.nms.Names'],
                 'o': ['op.obj.O'],
                 'obj': ['op.obj.Obj'],
                 'object': ['op.obj.Object'],
                 'objectlist': ['op.obj.ObjectList'],
                 'option': ['op.prs.Option'],
                 'output': ['op.opt.Output'],
                 'repeater': ['op.clk.Repeater'],
                 'request': ['urllib.request.Request'],
                 'rss': ['op.rss.Rss'],
                 'seen': ['op.rss.Seen'],
                 'setter': ['op.prs.Setter'],
                 'skip': ['op.prs.Skip'],
                 'textwrap': ['op.irc.TextWrap'],
                 'thr': ['op.thr.Thr'],
                 'timed': ['op.prs.Timed'],
                 'timer': ['op.clk.Timer'],
                 'todo': ['op.tdo.Todo'],
                 'token': ['op.prs.Token'],
                 'udp': ['op.udp.UDP'],
                 'urlerror': ['urllib.error.URLError'],
                 'user': ['op.usr.User'],
                 'users': ['op.usr.Users']
    })

    modules = Object({
                    'cfg': 'op.irc',
                    'cmd': 'op.cmd',
                    'dlt': 'op.usr',
                    'dne': 'op.tdo',
                    'dpl': 'op.rss',
                    'ech': 'op.adm',
                    'flt': 'op.adm',
                    'fnd': 'op.fnd',
                    'ftc': 'op.rss',
                    'krn': 'op.adm',
                    'log': 'op.log',
                    'mbx': 'op.mbx',
                    'met': 'op.usr',
                    'rem': 'op.rss',
                    'rss': 'op.rss',
                    'sve': 'op.adm',
                    'tdo': 'op.tdo',
                    'thr': 'op.adm',
                    'upt': 'op.adm',
                    'ver': 'op.adm'
    })

    inits =  Object({
                  'adm': 'op.adm',
                  'bus': 'op.bus',
                  'clk': 'op.clk',
                  'dbs': 'op.dbs',
                  'edt': 'op.edt',
                  'err': 'op.err',
                  'evt': 'op.evt',
                  'fnd': 'op.fnd',
                  'hdl': 'op.hdl',
                  'irc': 'op.irc',
                  'itr': 'op.itr',
                  'krn': 'op.krn',
                  'ldr': 'op.ldr',
                  'log': 'op.log',
                  'mbx': 'op.mbx',
                  'nms': 'op.nms',
                  'obj': 'op.obj',
                  'opt': 'op.opt',
                  'prs': 'op.prs',
                  'rss': 'op.rss',
                  'tdo': 'op.tdo',
                  'thr': 'op.thr',
                  'tms': 'op.tms',
                  'trc': 'op.trc',
                  'trm': 'op.trm',
                  'udp': 'op.udp',
                  'url': 'op.url',
                  'usr': 'op.usr',
                  'utl': 'op.utl',
                  'zzz': 'op.zzz'
    })

    @staticmethod
    def getnames(nm, dft=None):
        return Names.names.get(nm, dft)


    @staticmethod
    def getmodule(mn):
        return Names.modules.get(mn, None)

    @staticmethod
    def getinit(mn):
        return Names.inits.get(mn, None)

    @staticmethod
    def tbl(tbl):
        Names.names.update(tbl["names"])
        Names.modules.update(tbl["modules"])
        Names.inits.update(tbl["inits"])

    @staticmethod
    def walk(names):
        for mn in findall(names):
            mod = direct(mn)
            if "cmd" not in mn:
                Names.inits[mn.split(".")[-1]] = mn
            Names.modules.update(findmods(mod))
            for k, v in findnames(mod).items():
                if k not in Names.names:
                    Names.names[k] = []
                if v not in Loader.names[k]:
                    Names.names[k].append(v)
        