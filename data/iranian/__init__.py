from model.lang import Language

_FAMILY = 'iranian'

AVESTAN = Language('avestan', _FAMILY, extinct_year=-400)
KURMANJI = Language('kurmanji', _FAMILY, 16000000)
MAZANDARANI = Language('mazandarani', _FAMILY, 2400000)
OSSETIAN_DIGORON = Language('ossetian_digoron', _FAMILY, 100000)
OSSETIAN_IRON = Language('ossetian_iron', _FAMILY, 390000, 125000)
PASHTO = Language('pashto', _FAMILY, 54000000, 4800000)
PERSIAN = Language('persian', _FAMILY, 67000000, 41000000)
PERSIAN_MIDDLE = Language('persian_middle', _FAMILY, extinct_year=800)
PERSIAN_OLD = Language('persian_old', _FAMILY, extinct_year=-300)
SORANI = Language('sorani', _FAMILY, 5300000)
TAJIK = Language('tajik', _FAMILY, 8300000)
ZAZAKI = Language('zazaki', _FAMILY, 3500000)


IRANIAN = [
    AVESTAN,
    KURMANJI,
    MAZANDARANI,
    OSSETIAN_DIGORON,
    OSSETIAN_IRON,
    PASHTO,
    PERSIAN,
    PERSIAN_MIDDLE,
    PERSIAN_OLD,
    SORANI,
    TAJIK,
    ZAZAKI,
]
