from model.lang import Language

CHUMASH_CENTRAL = Language('chumash_central', __file__, extinct_year=1965)
KIOWA = Language('kiowa', __file__, 20)
PAWNEE = Language('pawnee', __file__, 4160)
QUECHUA = Language('quechua', __file__, 7200000)
TEWA = Language('tewa', __file__, 1600)
TOTONAC = Language('totonac', __file__, 260000)


NEW_WORLD_OTHER = [
    CHUMASH_CENTRAL,
    KIOWA,
    PAWNEE,
    QUECHUA,
    TEWA,
    TOTONAC,
]
