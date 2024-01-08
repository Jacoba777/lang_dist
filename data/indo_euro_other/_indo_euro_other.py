from model.lang import Language

FAMILY = 'indo_euro_other'

ALBANIAN = Language('albanian', FAMILY, 7500000, 0)
ARMENIAN = Language('armenian', FAMILY, 5300000, 0)
GREEK = Language('greek', FAMILY, 13500000, 0)
GREEK_ANCIENT = Language('greek_ancient', FAMILY, extinct_year=-300)
GREEK_MARIUPOL = Language('greek_mariupol', FAMILY, 20000, 0)
TOCHARIAN_A = Language('tocharian_a', FAMILY, extinct_year=800)
TOCHARIAN_B = Language('tocharian_b', FAMILY, extinct_year=800)


ALL_LANGS = [
    ALBANIAN,
    ARMENIAN,
    GREEK,
    GREEK_ANCIENT,
    GREEK_MARIUPOL,
    TOCHARIAN_A,
    TOCHARIAN_B,
]
