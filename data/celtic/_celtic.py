from model.lang import Language

FAMILY = 'celtic'

BRETON = Language('breton', FAMILY, 120000, 0)
CORNISH = Language('cornish', FAMILY, 0, 500, extinct_year=1777)
IRISH = Language('irish', FAMILY, 78000, 1900000)
IRISH_OLD = Language('irish_old', FAMILY, extinct_year=900)
MANX = Language('manx', FAMILY, 23, 2200)
SCOTTISH_GAELIC = Language('scottish_gaelic', FAMILY, 57000, 0)
WELSH = Language('welsh', FAMILY, 655000, 0)

ALL_LANGS = [
    BRETON,
    CORNISH,
    IRISH,
    IRISH_OLD,
    MANX,
    SCOTTISH_GAELIC,
    WELSH,
]
