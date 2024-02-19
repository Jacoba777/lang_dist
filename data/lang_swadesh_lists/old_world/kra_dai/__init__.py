from model.lang import Language

BUYANG = Language('buyang', __file__, 1500)
GELAO = Language('gelao', __file__, 7900)
HLAI = Language('hlai', __file__, 667000)
JIZHAO = Language('jizhao', __file__, 75)
KHAM_SOUTHERN = Language('kham_southern', __file__, 1500000)  # KAM?
LAO = Language('lao', __file__, 3000000)
ONG_BE = Language('ong_be', __file__, 600000)
SHAN = Language('shan', __file__, 4700000)
THAI = Language('thai', __file__, 21000000, 40000000)
ZHUANG = Language('zhuang', __file__, 16000000)


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
