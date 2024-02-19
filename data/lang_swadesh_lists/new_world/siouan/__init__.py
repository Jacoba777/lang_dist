from model.lang import Language

_family = 'siouan'

CROW = Language('crow', _family, 4160)
DAKOTA_SANTEE = Language('dakota_santee', _family, 290)  # Speakers are all dialects
DAKOTA_SISSETON = Language('dakota_sisseton', _family)
LAKOTA = Language('lakota', _family, 2100)
OSAGE = Language('osage', _family, extinct_year=2005, l2_speakers=17)
TUTELO = Language('tutelo', _family, extinct_year=1982)


SIOUAN = [
    CROW,
    DAKOTA_SANTEE,
    DAKOTA_SISSETON,
    LAKOTA,
    OSAGE,
    TUTELO,
]
