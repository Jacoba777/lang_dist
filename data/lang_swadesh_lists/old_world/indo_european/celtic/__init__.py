from model.lang import Language

_FAMILY = 'celtic'

BRETON = Language('breton', _FAMILY, 120000, 0)
CORNISH = Language('cornish', _FAMILY, 0, 500, extinct_year=1777)
IRISH = Language('irish', _FAMILY, 78000, 1900000)
IRISH_OLD = Language('irish_old', _FAMILY, extinct_year=900)
MANX = Language('manx', _FAMILY, 23, 2200)
SCOTTISH_GAELIC = Language('scottish_gaelic', _FAMILY, 57000, 0)
WELSH = Language('welsh', _FAMILY, 655000, 0)

CELTIC = [
    BRETON,
    CORNISH,
    IRISH,
    IRISH_OLD,
    MANX,
    SCOTTISH_GAELIC,
    WELSH,
]
