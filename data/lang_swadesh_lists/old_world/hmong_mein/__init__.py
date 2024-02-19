from model.lang import Language

HMONG_WHITE = Language('hmong_white', __file__, 8000000)
IU_MEIN = Language('iu_mein', __file__, 800000)


HMONG_MEIN = [
    HMONG_WHITE,
    IU_MEIN,
]
