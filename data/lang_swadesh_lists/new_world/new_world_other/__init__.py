from model.lang import Language

_family = 'new_world_other'

CHUMASH_CENTRAL = Language('chumash_central', _family, extinct_year=1965)
KIOWA = Language('kiowa', _family, 20)
PAWNEE = Language('pawnee', _family, 4160)
QUECHUA = Language('quechua', _family, 7200000)
TEWA = Language('tewa', _family, 1600)
TOTONAC = Language('totonac', _family, 260000)


NEW_WORLD_OTHER = [
    CHUMASH_CENTRAL,
    KIOWA,
    PAWNEE,
    QUECHUA,
    TEWA,
    TOTONAC,
]
