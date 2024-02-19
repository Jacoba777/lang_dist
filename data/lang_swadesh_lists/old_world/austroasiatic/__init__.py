from model.lang import Language

BAHNAR = Language('bahnar', __file__, 160000)
BLANG = Language('blang', __file__, 68000)
KATU = Language('katu', __file__, 23000)
KHASI = Language('khasi', __file__, 1000000)
KHMER = Language('khmer', __file__, 17000000, 1000000)
MON = Language('mon', __file__, 900000)
SANTALI = Language('santali', __file__, 7600000)
SEDANG = Language('sedang', __file__, 98000)
TEMIAR = Language('temiar', __file__, 30000)
VIETNAMESE = Language('vietnamese', __file__, 85000000)

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
