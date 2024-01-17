from model.lang import Language

FAMILY = 'slavic'

BELARUSIAN = Language('belarusian', FAMILY, 5100000, 1300000)
BULGARIAN = Language('bulgarian', FAMILY, 7600000, 2400000)
CHURCH_SLAVONIC_OLD = Language('church_slavonic_old', FAMILY, extinct_year=1000)
CZECH = Language('czech', FAMILY, 10700000, 0)
KASHUBIAN = Language('kashubian', FAMILY, 87600, 0)
MACEDONIAN = Language('macedonian', FAMILY, 2500000, 0)
POLABIAN = Language('polabian', FAMILY, 0, 5, extinct_year=1756)
POLISH = Language('polish', FAMILY, 40000000, 670000)
RUSSIAN = Language('russian', FAMILY, 150000000, 110000000)
RUSYN = Language('rusyn', FAMILY, 70000, 0)
SERBO_CROATIAN = Language('serbo_croatian', FAMILY, 19000000, 0)
SILESIAN = Language('silesian', FAMILY, 457900, 0)
SLOVAK = Language('slovak', FAMILY, 5000000, 2000000)
SLOVENE = Language('slovene', FAMILY, 2500000, 0)
SORBIAN_LOWER = Language('sorbian_lower', FAMILY, 6900, 0)
SORBIAN_UPPER = Language('sorbian_upper', FAMILY, 13000, 0)
UKRAINIAN = Language('ukrainian', FAMILY, 27000000, 5800000)

ALL_LANGS = [
    BELARUSIAN,
    BULGARIAN,
    CZECH,
    KASHUBIAN,
    MACEDONIAN,
    POLABIAN,
    POLISH,
    RUSSIAN,
    # RUSYN,  # need to fix data
    SERBO_CROATIAN,
    SILESIAN,
    SLOVAK,
    SLOVENE,
    SORBIAN_LOWER,
    SORBIAN_UPPER,
    UKRAINIAN,
]
