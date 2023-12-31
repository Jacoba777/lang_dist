from model.lang import Language

FAMILY = 'east_asian'

JAPANESE = Language('japanese', FAMILY, 128000000, 0)
KOREAN = Language('korean', FAMILY, 82000000, 0)


ALL_LANGS = [
    JAPANESE,
    KOREAN,
]
