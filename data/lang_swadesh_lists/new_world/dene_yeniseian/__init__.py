from model.lang import Language

_FAMILY = 'dene_yeniseian'

DENAINA = Language('denaina', _FAMILY, 5)
EYAK = Language('eyak', _FAMILY, extinct_year=2008)
HUPA = Language('hupa', _FAMILY, 1, 30)
KET = Language('ket', _FAMILY, 153)
KOTT = Language('kott', _FAMILY, extinct_year=1800)
NAVAJO = Language('navajo', _FAMILY, 170000)
SLAVEY_SOUTH = Language('slavey_south', _FAMILY, 1000)
TLINGIT = Language('tlingit', _FAMILY, 170, 10)

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
