from model.lang import Language

_family = 'constructed'

ESPERANTO = Language('esperanto', _family, 1000, 100000)
KLINGON = Language('klingon', _family, 0, 25)


CONSTRUCTED = [
    ESPERANTO,
    KLINGON,
]
