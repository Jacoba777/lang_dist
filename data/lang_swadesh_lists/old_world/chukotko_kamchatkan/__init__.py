from model.lang import Language

CHUKCHI = Language('chukchi', __file__, 8500)
ITELMEN = Language('itelmen', __file__, 80)
KEREK = Language('kerek', __file__, extinct_year=2005)
KORYAK = Language('koryak', __file__, 1665)

CHUKOTKO_KAMCHATKAN = [
    CHUKCHI,
    ITELMEN,
    KEREK,
    KORYAK,
]
