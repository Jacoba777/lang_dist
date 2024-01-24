from model.lang import Language

_FAMILY = 'dravidian'

TAMIL = Language('tamil', _FAMILY, 78000000, 8000000)
MALAYALAM = Language('malayalam', _FAMILY, 37000000, 700000)
KODAVA = Language('kodava', _FAMILY, 113900)
KANNADA = Language('kannada', _FAMILY, 44000000, 15000000)
TULU = Language('tulu', _FAMILY, 1850000)
TELUGU = Language('telugu', _FAMILY, 83000000, 13000000)
GONDI = Language('gondi', _FAMILY, 2980000)
KONDA_DARA = Language('konda_dara', _FAMILY, 61000)
KUI = Language('kui', _FAMILY, 941000)
KUVI = Language('kuvi', _FAMILY, 156000)
KOLAMI = Language('kolami', _FAMILY, 128000)
KURUKH = Language('kurukh', _FAMILY, 2280000)
BRAHUI = Language('brahui', _FAMILY, 2640000)


DRAVIDIAN = [
    TAMIL,
    MALAYALAM,
    KODAVA,
    KANNADA,
    TULU,
    TELUGU,
    GONDI,
    KONDA_DARA,
    KUI,
    KUVI,
    KOLAMI,
    KURUKH,
    BRAHUI,
]
