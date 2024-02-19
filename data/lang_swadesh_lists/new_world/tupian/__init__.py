from model.lang import Language

TUPI_OLD = Language('tupi_old', __file__, 1700)
GUARANI = Language('guaraní', __file__, 6500000)


TUPIAN = [
    TUPI_OLD,
    GUARANI,
]
