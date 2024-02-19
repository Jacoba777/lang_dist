from model.lang import Language

EVEN = Language('even', __file__, 5700)
EVENKI = Language('evenki', __file__, 16000)
MANCHU = Language('manchu', __file__, 20, 2000)
NANAI = Language('nanai', __file__, 1400)
NEGIDAL = Language('negidal', __file__, 10)
OROCH = Language('oroch', __file__, 43)
OROK = Language('orok', __file__, 30)
OROQEN = Language('oroqen', __file__, 3800)
UDEGE = Language('udege', __file__, 100)
ULCH = Language('ulch', __file__, 150)

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
