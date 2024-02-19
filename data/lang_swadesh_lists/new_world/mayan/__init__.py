from model.lang import Language

HUASTEC = Language('huastec', __file__, 170000)
ITZA = Language('itza', __file__, 410)
KICHE = Language('kiche', __file__, 1100000)
MAM = Language('mam', __file__, 610000)
MAYA_YUCATEC = Language('maya_yucatec', __file__, 800000)
QEQCHI = Language('qeqchi', __file__, 1300000)
TZOTZIL = Language('tzotzil', __file__, 550000)

MAYAN = [
    HUASTEC,
    ITZA,
    KICHE,
    MAM,
    MAYA_YUCATEC,
    QEQCHI,
    TZOTZIL,
]
