from model.lang import Language

_family = 'north_american_other'

CHUMASH_CENTRAL = Language('chumash_central', _family, extinct_year=1965)
KIOWA = Language('kiowa', _family, 20)
PAWNEE = Language('pawnee', _family, 4160)
TEWA = Language('tewa', _family, 1600)


NORTH_AMERICAN_OTHER = [
    CHUMASH_CENTRAL,
    KIOWA,
    PAWNEE,
    TEWA,
]
