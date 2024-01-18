from model.lang import Language

FAMILY = 'dravidian'

TAMIL = Language('tamil', FAMILY, 78000000, 8000000)
MALAYALAM = Language('malayalam', FAMILY, 37000000, 700000)
KODAVA = Language('kodava', FAMILY, 113900)
KANNADA = Language('kannada', FAMILY, 44000000, 15000000)
TULU = Language('tulu', FAMILY, 1850000)
TELUGU = Language('telugu', FAMILY, 83000000, 13000000)
GONDI = Language('gondi', FAMILY, 2980000)
KONDA_DARA = Language('konda_dara', FAMILY, 61000)
KUI = Language('kui', FAMILY, 941000)
KUVI = Language('kuvi', FAMILY, 156000)
KOLAMI = Language('kolami', FAMILY, 128000)
KURUKH = Language('kurukh', FAMILY, 2280000)
BRAHUI = Language('brahui', FAMILY, 2640000)


ALL_LANGS = [
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
