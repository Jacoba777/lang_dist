from model.lang import Language

_FAMILY = 'algic'

BLACKFOOT = Language('blackfoot', _FAMILY, 2900)
MIKMAQ = Language('mikmaq', _FAMILY, 7140)
OJIBWE = Language('ojibwe', _FAMILY, 50000)
UNAMI = Language('unami', _FAMILY, extinct_year=2002)

ALGIC = [
    BLACKFOOT,
    MIKMAQ,
    OJIBWE,
    UNAMI,
]
