# This file is placed in the Public Domain.


"""Prosecutor. Reconsider. OTP-CR-117/19."""


from hdl import Commands


txt1 = "@IntlCrimCourt @Europol @POL_DenHaag @Het_OM ask @KarimKhanQC to reconsider OTP-CR-117/19"
txt2 = "Elderly Handicapped (Wzd) Psychatric Patients (WvGGZ) Criminals (Wfz)"
txt3 = "Elderly & Handicapped/Wzd Psychatric Patients/WvGGZ Criminals/Wfz @IntlCrimCourt @KarimKhanQC article 15, reconsider OTP-CR-117/19"
txt4 = "Elderly & Handicapped/Wzd Psychatric Patients/WvGGZ Criminals/Wfz - @IntlCrimCourt @KarimKhanQC, article 15, reconsider OTP-CR-117/19 - http://genocide.rtfd.io"
txt5 = "@KarimKhanQC @IntlCrimCourt Stop Genocide. Article 15 needs no cooperation. Reconsider OTP-CR-117/19 - https://genocide.rtfd.io/reconsider.html #ggz"


def slg(event):
    event.reply(txt5)


Commands.add(slg)
