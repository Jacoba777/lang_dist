from model.lang import Language

_family = 'mayan'

HUASTEC = Language('huastec', _family, 170000)
ITZA = Language('itza', _family, 410)
KICHE = Language('kiche', _family, 1100000)
MAM = Language('mam', _family, 610000)
MAYA_YUCATEC = Language('maya_yucatec', _family, 800000)
QEQCHI = Language('qeqchi', _family, 1300000)
TZOTZIL = Language('tzotzil', _family, 550000)

MAYAN = [
    HUASTEC,
    ITZA,
    KICHE,
    MAM,
    MAYA_YUCATEC,
    QEQCHI,
    TZOTZIL,
]
