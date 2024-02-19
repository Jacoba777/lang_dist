from model.lang import Language

TAMIL = Language('tamil', __file__, 78000000, 8000000)
MALAYALAM = Language('malayalam', __file__, 37000000, 700000)
KODAVA = Language('kodava', __file__, 113900)
KANNADA = Language('kannada', __file__, 44000000, 15000000)
TULU = Language('tulu', __file__, 1850000)
TELUGU = Language('telugu', __file__, 83000000, 13000000)
GONDI = Language('gondi', __file__, 2980000)
KONDA_DARA = Language('konda_dara', __file__, 61000)
KUI = Language('kui', __file__, 941000)
KUVI = Language('kuvi', __file__, 156000)
KOLAMI = Language('kolami', __file__, 128000)
KURUKH = Language('kurukh', __file__, 2280000)
BRAHUI = Language('brahui', __file__, 2640000)


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
