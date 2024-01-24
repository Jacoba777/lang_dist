from model.lang import Language

_FAMILY = 'koreanic'

JEJU = Language('jeju', _FAMILY, 5000)
KOREAN = Language('korean', _FAMILY, 82000000, 0)


KOREANIC = [
    JEJU,
    KOREAN,
]
