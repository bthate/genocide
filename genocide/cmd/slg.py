# This file is placed in the Public Domain.


"""Court. Prosecutor. Stop Genocide. Reconsider OTP-CR-117/19."""


from ..hdl import Commands


txt1 = "@IntlCrimCourt @Europol @POL_DenHaag @Het_OM ask @KarimKhanQC to reconsider OTP-CR-117/19"
txt2 = "Elderly Handicapped (Wzd) Psychatric Patients (WvGGZ) Criminals (Wfz)"
txt3 = "Elderly & Handicapped/Wzd Psychatric Patients/WvGGZ Criminals/Wfz @IntlCrimCourt @KarimKhanQC article 15, reconsider OTP-CR-117/19"
txt4 = "Elderly & Handicapped/Wzd Psychatric Patients/WvGGZ Criminals/Wfz - @IntlCrimCourt @KarimKhanQC, article 15, reconsider OTP-CR-117/19 - http://genocide.rtfd.io"
txt5 = "Stop Genocide. @KarimKhanQC @IntlCrimCourt, Reconsider OTP-CR-117/19 https://genocide.rtfd.io/ #ASP20 #ASP21 #ggz @Het_OM @adnl"
txt6 = "Court. Prosecutor. Stop Genocide. Reconsider OTP-CR-117/19. @IntlCrimCourt @KarimKhanQC - https://pypi.org/project/genocide/ #ASP21 #stopgenocide #ggz"


def slg(event):
    event.reply(txt6)


Commands.add(slg)
