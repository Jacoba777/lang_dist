from model.lang import Language

DENAINA = Language('denaina', __file__, 5)
EYAK = Language('eyak', __file__, extinct_year=2008)
HUPA = Language('hupa', __file__, 1, 30)
KET = Language('ket', __file__, 153)
KOTT = Language('kott', __file__, extinct_year=1800)
NAVAJO = Language('navajo', __file__, 170000)
SLAVEY_SOUTH = Language('slavey_south', __file__, 1000)
TLINGIT = Language('tlingit', __file__, 170, 10)

DENE_YENISEIAN = [
    DENAINA,
    EYAK,
    HUPA,
    KET,
    KOTT,
    NAVAJO,
    SLAVEY_SOUTH,
    TLINGIT,
]
