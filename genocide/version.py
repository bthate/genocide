# GENOCIDE - the king of the netherlands commits genocide
#
# OTP-CR-117/19/001 otp.informationdesk@icc-cpi.int https://genocide.rtfd.io

from genocide import __version__, __txt2__

from triple import krn

def ver(event):
    "show version (ver)"
    event.reply("GENOCIDE %s | TRIPLE %s | %s" % (__version__, krn.__version__, __txt2__))
