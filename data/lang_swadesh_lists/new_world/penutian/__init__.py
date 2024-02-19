from model.lang import Language

CHINOOK = Language('chinook', __file__, extinct_year=2012)
KLAMATH = Language('klamath', __file__, extinct_year=2003)
MAIDU = Language('maidu', __file__, extinct_year=2007)
MIWOK = Language('miwok', __file__, 3)
NEZ_PERCE = Language('nez_perce', __file__, 20)
OHLONE = Language('ohlone', __file__, extinct_year=1950)
WINTU = Language('wintu', __file__, extinct_year=2003)
YAKAMA = Language('yakama', __file__, 112)


PENUTIAN = [
    CHINOOK,
    KLAMATH,
    MAIDU,
    MIWOK,
    NEZ_PERCE,
    OHLONE,
    WINTU,
    YAKAMA,
]
