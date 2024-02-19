from model.lang import Language

ABINOMN = Language('abinomn', __file__, 300)
AINU = Language('ainu', __file__, 2, 10)
BASQUE = Language('basque', __file__, 750000)
BURUSHASKI = Language('burushaski', __file__, 112000)
ELAMITE = Language('elamite', __file__, extinct_year=1000)
ETRUSCAN = Language('etruscan', __file__, extinct_year=50)
HUAVE = Language('huave', __file__, 20000)
NIVKH = Language('nivkh', __file__, 198)
PUREPECHA = Language('purepecha', __file__, 140000)
SUMERIAN = Language('sumerian', __file__, extinct_year=100)
YUKAGHIR_TUNDRA = Language('yukaghir_tundra', __file__, 320)
YUPIK_CENTRAL_SIBERIAN = Language('yupik_central_siberian', __file__, 1200)
ZUNI = Language('zuni', __file__, 9600)

ISOLATES = [
    ABINOMN,
    AINU,
    BASQUE,
    BURUSHASKI,
    ELAMITE,
    ETRUSCAN,
    HUAVE,
    NIVKH,
    PUREPECHA,
    SUMERIAN,
    YUKAGHIR_TUNDRA,
    YUPIK_CENTRAL_SIBERIAN,
    ZUNI,
]
