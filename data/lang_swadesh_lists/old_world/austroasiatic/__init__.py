from model.lang import Language

_FAMILY = 'austroasiatic'

BAHNAR = Language('bahnar', _FAMILY, 160000)
BLANG = Language('blang', _FAMILY, 68000)
KATU = Language('katu', _FAMILY, 23000)
KHASI = Language('khasi', _FAMILY, 1000000)
KHMER = Language('khmer', _FAMILY, 17000000, 1000000)
MON = Language('mon', _FAMILY, 900000)
SANTALI = Language('santali', _FAMILY, 7600000)
SEDANG = Language('sedang', _FAMILY, 98000)
TEMIAR = Language('temiar', _FAMILY, 30000)
VIETNAMESE = Language('vietnamese', _FAMILY, 85000000)

AUSTROASIATIC = [
    BAHNAR,
    BLANG,
    KATU,
    KHASI,
    KHMER,
    MON,
    SANTALI,
    SEDANG,
    VIETNAMESE,
]
