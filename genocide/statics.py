# This file is placed in the Public Domain.


"tables"


CORE = {
    "booting": "2edf1cefde5ab25d23687d22459016cd",
    "brokers": "dd4e4a6d6f110b6a2e7fc4df72db71ea",
    "clients": "9bd824df44ceeeaf73134e38f8177669",
    "command": "937de1c33d195330eb1d312775fee576",
    "configs": "55373ef42c73f1df77f0a29755fe6027",
    "daemons": "499c578e38cadc0a6fb4f005e858944d",
    "defines": "26bb19465bc1c9cdd82ad192696238a0",
    "encoder": "7c7f68bbcdc0bd9955c0acf70a9b4d7c",
    "engines": "767e741a9e84f56cdb1b68c979a6b584",
    "hashing": "1b7cb34eaff614661f28ad870299ba98",
    "message": "6c2322224bbca893fd5899bda65df43e",
    "methods": "dc4c2e41f7a6cf82584e8119ee6725fa",
    "objects": "529a55e137b6f5bd5908fdcdd1049d86",
    "outputs": "b7edddf1249f1be8b9e568379479948f",
    "package": "c1fa926069d773af8863d6d29401fa6f",
    "parsers": "cc9923d5e2e0aab885247a530ac0970c",
    "persist": "49e11f383821f99816f40c5bf2e304d6",
    "repeats": "82c2d2a922b8e7d6c8a0fa5d48bf5ce7",
    "require": "53ae8d308fceff8dab77fc89f86f7eef",
    "runtime": "fd61caa2c505c1d381eda8b97cae7262",
    "threads": "89d6c338a08271a7ce8f21e624ce9fe6",
    "timings": "3779158dd2a2f280d403717c7ea75886",
    "utility": "370494b1ecafd52182d8ad2a1192f866"
}


MODULES = {
    "mdl": "6e3368b0f7cf605e9addbb67fee4c8d0",
    "pth": "3067097a3f2fe46facc9920fac04bd00",
    "req": "bc1984d2e9de0310dc1b468f25c7ab8c",
    "slg": "e68f11973ddc2e3edeb0de0e16e9fe7a",
    "ver": "232df33c5aab9214146ac3cf2ce6df63"
}


NAMES = {
    "dis": "mdl",
    "now": "mdl",
    "pth": "pth",
    "req": "req",
    "slg": "slg",
    "ver": "ver"
}


def __dir__():
    return (
        'CORE',
        'MODULES',
        'NAMES'
    )
