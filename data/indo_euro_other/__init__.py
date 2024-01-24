from model.lang import Language

_FAMILY = 'indo_euro_other'

ALBANIAN = Language('albanian', _FAMILY, 7500000, 0)
ARMENIAN = Language('armenian', _FAMILY, 5300000, 0)
GREEK = Language('greek', _FAMILY, 13500000, 0)
GREEK_ANCIENT = Language('greek_ancient', _FAMILY, extinct_year=-300)
GREEK_MARIUPOL = Language('greek_mariupol', _FAMILY, 20000, 0)
HITTITE = Language('hittite', _FAMILY, extinct_year=-1200)
LUWIAN = Language('luwian', _FAMILY, extinct_year=-600)
TOCHARIAN_A = Language('tocharian_a', _FAMILY, extinct_year=800)
TOCHARIAN_B = Language('tocharian_b', _FAMILY, extinct_year=800)


INDO_EURO_OTHER = [
    ALBANIAN,
    ARMENIAN,
    GREEK,
    GREEK_ANCIENT,
    GREEK_MARIUPOL,
    TOCHARIAN_A,
    TOCHARIAN_B,
]
