from model.lang import Language

AMAMI_OSHIMA_NORTHERN = Language('amami_oshima_northern', __file__, 12000)
AMAMI_OSHIMA_SOUTHERN = Language('amami_oshima_southern', __file__, 1800)
JAPANESE = Language('japanese', __file__, 128000000)
KIKAI = Language('kikai', __file__, 13000)
KUNIGAMI = Language('kunigami', __file__, 5000)
MIYAKO = Language('miyako', __file__, 68000)
OKI_NO_ERABU = Language('oki_no_erabu', __file__, 3200)
OKINAWAN = Language('okinawan', __file__, 100000)
TOKU_NO_SHIMA = Language('toku_no_shima', __file__, 5100)
YAEYAMA = Language('yaeyama', __file__, 47600)
YONAGUNI = Language('yonaguni', __file__, 400)
YORON = Language('yoron', __file__, 950)

JAPONIC = [
    AMAMI_OSHIMA_NORTHERN,
    AMAMI_OSHIMA_SOUTHERN,
    JAPANESE,
    KIKAI,
    KUNIGAMI,
    MIYAKO,
    OKI_NO_ERABU,
    OKINAWAN,
    TOKU_NO_SHIMA,
    YAEYAMA,
    YONAGUNI,
    YORON,
]
