from model.lang import Language

AVESTAN = Language('avestan', __file__, extinct_year=-400)
KURMANJI = Language('kurmanji', __file__, 16000000)
MAZANDARANI = Language('mazandarani', __file__, 2400000)
OSSETIAN_DIGORON = Language('ossetian_digoron', __file__, 100000)
OSSETIAN_IRON = Language('ossetian_iron', __file__, 390000, 125000)
PASHTO = Language('pashto', __file__, 54000000, 4800000)
PERSIAN = Language('persian', __file__, 67000000, 41000000)
PERSIAN_MIDDLE = Language('persian_middle', __file__, extinct_year=800)
PERSIAN_OLD = Language('persian_old', __file__, extinct_year=-300)
SORANI = Language('sorani', __file__, 5300000)
TAJIK = Language('tajik', __file__, 8300000)
ZAZAKI = Language('zazaki', __file__, 3500000)


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
