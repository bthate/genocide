# This file is placed in the Public Domain

"""GENOCIDE(1)			   User Commands 			 GENOCIDE(1)

NAME
        GENOCIDE - using the law to administer poison equals genocide.

SYNOPSIS
        1) gcd <cmd> [mods=mod1,mod2] [-d] [-h] [-s] [-v]
        2) gcd cfg server=<server> channel=<channel> nick=<nick>
        3) gcd met <userhost>
        4) gcd rss <url>
        5) gcd ftc
        6) gcd cmd
        7) gcd mods=irc

DESCRIPTION
        GENOCIDE is a python3 program that holds evidence that the king of the
        netherlands is doing a genocide, a written response where the king of
        the netherlands  confirmed taking note of “what i have written”, namely
        proof that medicine he uses in treatement laws like zyprexa, haldol,
        abilify and clozapine are poison. This means that the king of the
        netherlands is not using laws to provide care for the elderly,
        handicapped, psychiatric patients and criminals but is using these laws
        to administer poison. Poison that makes impotent, is both physical
        (contracted muscles) and mental (let people hallucinate) torture and
        kills members of the victim groups.

        GENOCIDE shows correspondence with the Internationnal Criminal Court
        about the genocide of the king of the netherlands (using the law to
        administer poison), including stats on suicide while the king of the
        netherland's genocide is still going on. Status is that there is not
        a basis to proceed, whether the king of the netherland's genocide
        doesn’t fit the description or the netherlands doesn’t want to
        cooperate with stopping the genocide the king of the netherlands is
        doing.

        GENOCIDE provides a IRC bot that can run as a background daemon for
        24/7 a day presence in a IRC channel. You can use it to display RSS
        feeds, act as a UDP to IRC gateway, program your own commands for it
        and have it log objects on disk to search them.

        GENOCIDE is placed in the Public Domain, no COPYRIGHT, no LICENSE.
        
OPTIONS
        -r		use /var/lib/genocide/
        -s              start a shell
        -v              be verbose
        -h              print this message
"""

def hlp(event):
    print(__doc__)
