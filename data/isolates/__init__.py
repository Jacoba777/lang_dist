from model.lang import Language

_FAMILY = 'isolates'

ABINOMN = Language('abinomn', _FAMILY, 300)
AINU = Language('ainu', _FAMILY, 2, 10)
BASQUE = Language('basque', _FAMILY, 750000)
BURUSHASKI = Language('burushaski', _FAMILY, 112000)
ELAMITE = Language('elamite', _FAMILY, extinct_year=1000)
ETRUSCAN = Language('etruscan', _FAMILY, extinct_year=50)
NIVKH = Language('nivkh', _FAMILY, 198)
SUMERIAN = Language('sumerian', _FAMILY, extinct_year=100)
YUKAGHIR_TUNDRA = Language('yukaghir_tundra', _FAMILY, 320)
YUPIK_CENTRAL_SIBERIAN = Language('yupik_central_siberian', _FAMILY, 1200)

ISOLATES = [
    ABINOMN,
    AINU,
    BASQUE,
    BURUSHASKI,
    ELAMITE,
    ETRUSCAN,
    NIVKH,
    SUMERIAN,
    YUKAGHIR_TUNDRA,
    YUPIK_CENTRAL_SIBERIAN,
]
