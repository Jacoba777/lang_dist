from model.lang import Language

FAMILY = 'iranian'

AVESTAN = Language('avestan', FAMILY, extinct_year=-400)
KURMANJI = Language('kurmanji', FAMILY, 16000000)
MAZANDARANI = Language('mazandarani', FAMILY, 2400000)
OSSETIAN_DIGORON = Language('ossetian_digoron', FAMILY, 100000)
OSSETIAN_IRON = Language('ossetian_iron', FAMILY, 390000, 125000)
PASHTO = Language('pashto', FAMILY, 54000000, 4800000)
PERSIAN = Language('persian', FAMILY, 67000000, 41000000)
PERSIAN_MIDDLE = Language('persian_middle', FAMILY, extinct_year=800)
PERSIAN_OLD = Language('persian_old', FAMILY, extinct_year=-300)
SORANI = Language('sorani', FAMILY, 5300000)
TAJIK = Language('tajik', FAMILY, 8300000)
ZAZAKI = Language('zazaki', FAMILY, 3500000)


ALL_LANGS = [
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
