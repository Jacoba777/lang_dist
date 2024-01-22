from model.lang import Language

FAMILY = 'isolates'

AINU = Language('ainu', FAMILY, 2, 10)
BASQUE = Language('basque', FAMILY, 750000)
BURUSHASKI = Language('burushaski', FAMILY, 112000)
ELAMITE = Language('elamite', FAMILY, extinct_year=1000)
ETRUSCAN = Language('etruscan', FAMILY, extinct_year=50)
NIVKH = Language('nivkh', FAMILY, 198)
SUMERIAN = Language('sumerian', FAMILY, extinct_year=100)
YUKAGHIR_TUNDRA = Language('yukaghir_tundra', FAMILY, 320)
YUPIK_CENTRAL_SIBERIAN = Language('yupik_central_siberian', FAMILY, 1200)

ALL_LANGS = [
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
