from model.lang import Language

FAMILY = 'chukotko_kamchatkan'

CHUKCHI = Language('chukchi', FAMILY, 8500)
ITELMEN = Language('itelmen', FAMILY, 80)
KEREK = Language('kerek', FAMILY, extinct_year=2005)
KORYAK = Language('koryak', FAMILY, 1665)

ALL_LANGS = [
    CHUKCHI,
    ITELMEN,
    KEREK,
    KORYAK,
]
