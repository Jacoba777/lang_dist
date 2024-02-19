from model.lang import Language

CROW = Language('crow', __file__, 4160)
DAKOTA_SANTEE = Language('dakota_santee', __file__, 290)  # Speakers are all dialects
DAKOTA_SISSETON = Language('dakota_sisseton', __file__)
LAKOTA = Language('lakota', __file__, 2100)
OSAGE = Language('osage', __file__, extinct_year=2005, l2_speakers=17)
TUTELO = Language('tutelo', __file__, extinct_year=1982)


SIOUAN = [
    CROW,
    DAKOTA_SANTEE,
    DAKOTA_SISSETON,
    LAKOTA,
    OSAGE,
    TUTELO,
]
