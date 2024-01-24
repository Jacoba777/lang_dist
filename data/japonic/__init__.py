from model.lang import Language

_FAMILY = 'japonic'

AMAMI_OSHIMA_NORTHERN = Language('amami_oshima_northern', _FAMILY, 12000)
AMAMI_OSHIMA_SOUTHERN = Language('amami_oshima_southern', _FAMILY, 1800)
JAPANESE = Language('japanese', _FAMILY, 128000000)
KIKAI = Language('kikai', _FAMILY, 13000)
KUNIGAMI = Language('kunigami', _FAMILY, 5000)
MIYAKO = Language('miyako', _FAMILY, 68000)
OKI_NO_ERABU = Language('oki_no_erabu', _FAMILY, 3200)
OKINAWAN = Language('okinawan', _FAMILY, 100000)
TOKU_NO_SHIMA = Language('toku_no_shima', _FAMILY, 5100)
YAEYAMA = Language('yaeyama', _FAMILY, 47600)
YONAGUNI = Language('yonaguni', _FAMILY, 400)
YORON = Language('yoron', _FAMILY, 950)

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
