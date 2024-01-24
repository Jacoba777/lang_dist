from model.lang import Language

FAMILY = 'japonic'

AMAMI_OSHIMA_NORTHERN = Language('amami_oshima_northern', FAMILY, 12000)
AMAMI_OSHIMA_SOUTHERN = Language('amami_oshima_southern', FAMILY, 1800)
JAPANESE = Language('japanese', FAMILY, 128000000)
KIKAI = Language('kikai', FAMILY, 13000)
KUNIGAMI = Language('kunigami', FAMILY, 5000)
MIYAKO = Language('miyako', FAMILY, 68000)
OKI_NO_ERABU = Language('oki_no_erabu', FAMILY, 3200)
OKINAWAN = Language('okinawan', FAMILY, 100000)
TOKU_NO_SHIMA = Language('toku_no_shima', FAMILY, 5100)
YAEYAMA = Language('yaeyama', FAMILY, 47600)
YONAGUNI = Language('yonaguni', FAMILY, 400)
YORON = Language('yoron', FAMILY, 950)

ALL_LANGS = [
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
