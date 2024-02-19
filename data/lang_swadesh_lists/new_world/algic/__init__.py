from model.lang import Language

BLACKFOOT = Language('blackfoot', __file__, 2900)
MIKMAQ = Language('mikmaq', __file__, 7140)
OJIBWE = Language('ojibwe', __file__, 50000)
UNAMI = Language('unami', __file__, extinct_year=2002)

ALGIC = [
    BLACKFOOT,
    MIKMAQ,
    OJIBWE,
    UNAMI,
]
