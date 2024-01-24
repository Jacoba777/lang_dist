from model.lang import Language

FAMILY = 'tungusic'

EVEN = Language('even', FAMILY, 5700)
EVENKI = Language('evenki', FAMILY, 16000)
MANCHU = Language('manchu', FAMILY, 20, 2000)
NANAI = Language('nanai', FAMILY, 1400)
NEGIDAL = Language('negidal', FAMILY, 10)
OROCH = Language('oroch', FAMILY, 43)
OROK = Language('orok', FAMILY, 30)
OROQEN = Language('oroqen', FAMILY, 3800)
UDEGE = Language('udege', FAMILY, 100)
ULCH = Language('ulch', FAMILY, 150)

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
