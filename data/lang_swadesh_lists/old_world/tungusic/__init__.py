from model.lang import Language

_FAMILY = 'tungusic'

EVEN = Language('even', _FAMILY, 5700)
EVENKI = Language('evenki', _FAMILY, 16000)
MANCHU = Language('manchu', _FAMILY, 20, 2000)
NANAI = Language('nanai', _FAMILY, 1400)
NEGIDAL = Language('negidal', _FAMILY, 10)
OROCH = Language('oroch', _FAMILY, 43)
OROK = Language('orok', _FAMILY, 30)
OROQEN = Language('oroqen', _FAMILY, 3800)
UDEGE = Language('udege', _FAMILY, 100)
ULCH = Language('ulch', _FAMILY, 150)

TUNGUSIC = [
    EVEN,
    EVENKI,
    MANCHU,
    NANAI,
    NEGIDAL,
    OROCH,
    OROK,
    OROQEN,
    UDEGE,
    ULCH,
]
