from model.lang import Language

ALBANIAN = Language('albanian', __file__, 7500000, 0)
ARMENIAN = Language('armenian', __file__, 5300000, 0)
GREEK = Language('greek', __file__, 13500000, 0)
GREEK_ANCIENT = Language('greek_ancient', __file__, extinct_year=-300)
GREEK_MARIUPOL = Language('greek_mariupol', __file__, 20000, 0)
HITTITE = Language('hittite', __file__, extinct_year=-1200)
LUWIAN = Language('luwian', __file__, extinct_year=-600)
TOCHARIAN_A = Language('tocharian_a', __file__, extinct_year=800)
TOCHARIAN_B = Language('tocharian_b', __file__, extinct_year=800)


INDO_EURO_OTHER = [
    ALBANIAN,
    ARMENIAN,
    GREEK,
    GREEK_ANCIENT,
    GREEK_MARIUPOL,
    TOCHARIAN_A,
    TOCHARIAN_B,
]
