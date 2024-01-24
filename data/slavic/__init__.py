from model.lang import Language

_FAMILY = 'slavic'

BELARUSIAN = Language('belarusian', _FAMILY, 5100000, 1300000)
BULGARIAN = Language('bulgarian', _FAMILY, 7600000, 2400000)
CHURCH_SLAVONIC_OLD = Language('church_slavonic_old', _FAMILY, extinct_year=1000)
CZECH = Language('czech', _FAMILY, 10700000, 0)
KASHUBIAN = Language('kashubian', _FAMILY, 87600, 0)
MACEDONIAN = Language('macedonian', _FAMILY, 2500000, 0)
POLABIAN = Language('polabian', _FAMILY, 0, 5, extinct_year=1756)
POLISH = Language('polish', _FAMILY, 40000000, 670000)
RUSSIAN = Language('russian', _FAMILY, 150000000, 110000000)
RUSYN = Language('rusyn', _FAMILY, 70000, 0)
SERBO_CROATIAN = Language('serbo_croatian', _FAMILY, 19000000, 0)
SILESIAN = Language('silesian', _FAMILY, 457900, 0)
SLOVAK = Language('slovak', _FAMILY, 5000000, 2000000)
SLOVENE = Language('slovene', _FAMILY, 2500000, 0)
SORBIAN_LOWER = Language('sorbian_lower', _FAMILY, 6900, 0)
SORBIAN_UPPER = Language('sorbian_upper', _FAMILY, 13000, 0)
UKRAINIAN = Language('ukrainian', _FAMILY, 27000000, 5800000)

SLAVIC = [
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
