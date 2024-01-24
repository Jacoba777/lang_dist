from model.lang import Language

_FAMILY = 'baltic'

LATGALIAN = Language('latgalian', _FAMILY, 200000, 0)
LATVIAN = Language('latvian', _FAMILY, 1500000, 0)
LITHUANIAN = Language('lithuanian', _FAMILY, 3000000, 0)
PRUSSIAN_OLD = Language('prussian_old', _FAMILY, extinct_year=1700)
SAMOGITIAN = Language('samogitian', _FAMILY, 500000, 0)


BALTIC = [
    LATGALIAN,
    LATVIAN,
    LITHUANIAN,
    PRUSSIAN_OLD,
    SAMOGITIAN,
]
