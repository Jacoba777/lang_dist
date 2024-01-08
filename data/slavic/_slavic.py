from model.lang import Language

FAMILY = 'slavic'

BELARUSIAN = Language('belarusian', FAMILY, 5100000, 1300000)
RUSSIAN = Language('russian', FAMILY, 150000000, 110000000)
RUSYN = Language('rusyn', FAMILY, 70000, 0)
UKRAINIAN = Language('ukrainian', FAMILY, 27000000, 5800000)

ALL_LANGS = [
    BELARUSIAN,
    RUSSIAN,
    RUSYN,
    UKRAINIAN,
]
