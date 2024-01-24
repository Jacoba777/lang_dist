from model.lang import Language

_FAMILY = 'chukotko_kamchatkan'

CHUKCHI = Language('chukchi', _FAMILY, 8500)
ITELMEN = Language('itelmen', _FAMILY, 80)
KEREK = Language('kerek', _FAMILY, extinct_year=2005)
KORYAK = Language('koryak', _FAMILY, 1665)

CHUKOTKO_KAMCHATKAN = [
    CHUKCHI,
    ITELMEN,
    KEREK,
    KORYAK,
]
