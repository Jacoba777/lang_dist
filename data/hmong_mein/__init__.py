from model.lang import Language

_FAMILY = 'hmong_mein'

HMONG_WHITE = Language('hmong_white', _FAMILY, 8000000)
IU_MEIN = Language('iu_mein', _FAMILY, 800000)


HMONG_MEIN = [
    HMONG_WHITE,
    IU_MEIN,
]
