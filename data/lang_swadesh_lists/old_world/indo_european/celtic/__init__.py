from model.lang import Language

BRETON = Language('breton', __file__, 120000, 0)
CORNISH = Language('cornish', __file__, 0, 500, extinct_year=1777)
IRISH = Language('irish', __file__, 78000, 1900000)
IRISH_OLD = Language('irish_old', __file__, extinct_year=900)
MANX = Language('manx', __file__, 23, 2200)
SCOTTISH_GAELIC = Language('scottish_gaelic', __file__, 57000, 0)
WELSH = Language('welsh', __file__, 655000, 0)

CELTIC = [
    BRETON,
    CORNISH,
    IRISH,
    IRISH_OLD,
    MANX,
    SCOTTISH_GAELIC,
    WELSH,
]
