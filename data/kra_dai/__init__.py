from model.lang import Language

_FAMILY = 'kra_dai'

BUYANG = Language('buyang', _FAMILY, 1500)
GELAO = Language('gelao', _FAMILY, 7900)
HLAI = Language('hlai', _FAMILY, 667000)
JIZHAO = Language('jizhao', _FAMILY, 75)
KHAM_SOUTHERN = Language('kham_southern', _FAMILY, 1500000)  # KAM?
LAO = Language('lao', _FAMILY, 3000000)
ONG_BE = Language('ong_be', _FAMILY, 600000)
SHAN = Language('shan', _FAMILY, 4700000)
THAI = Language('thai', _FAMILY, 21000000, 40000000)
ZHUANG = Language('zhuang', _FAMILY, 16000000)


KRA_DAI = [
    BUYANG,
    GELAO,
    HLAI,
    JIZHAO,
    KHAM_SOUTHERN,
    LAO,
    ONG_BE,
    SHAN,
    THAI,
    ZHUANG,
]
