from model.lang import Language

FAMILY = 'koreanic'

JEJU = Language('jeju', FAMILY, 5000)
KOREAN = Language('korean', FAMILY, 82000000, 0)


ALL_LANGS = [
    JEJU,
    KOREAN,
]
