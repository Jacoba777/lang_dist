from model.lang import Language

FAMILY = 'isolates'

BASQUE = Language('basque', FAMILY, 750000)
BURUSHASKI = Language('burushaski', FAMILY, 112000)
ELAMITE = Language('elamite', FAMILY, extinct_year=1000)
ETRUSCAN = Language('etruscan', FAMILY, extinct_year=50)
SUMERIAN = Language('sumerian', FAMILY, extinct_year=100)

ALL_LANGS = [
    BASQUE,
    BURUSHASKI,
    ELAMITE,
    ETRUSCAN,
    SUMERIAN,
]
