from model.lang import Language

_family = 'penutian'

CHINOOK = Language('chinook', _family, extinct_year=2012)
KLAMATH = Language('klamath', _family, extinct_year=2003)
MAIDU = Language('maidu', _family, extinct_year=2007)
MIWOK = Language('miwok', _family, 3)
NEZ_PERCE = Language('nez_perce', _family, 20)
OHLONE = Language('ohlone', _family, extinct_year=1950)
WINTU = Language('wintu', _family, extinct_year=2003)
YAKAMA = Language('yakama', _family, 112)


PENUTIAN = [
    CHINOOK,
    KLAMATH,
    MAIDU,
    MIWOK,
    NEZ_PERCÉ,
    OHLONE,
    WINTU,
    YAKAMA,
]
