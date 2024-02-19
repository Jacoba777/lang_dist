from model.lang import Language

BELARUSIAN = Language('belarusian', __file__, 5100000, 1300000)
BULGARIAN = Language('bulgarian', __file__, 7600000, 2400000)
CHURCH_SLAVONIC_OLD = Language('church_slavonic_old', __file__, extinct_year=1000)
CZECH = Language('czech', __file__, 10700000, 0)
KASHUBIAN = Language('kashubian', __file__, 87600, 0)
MACEDONIAN = Language('macedonian', __file__, 2500000, 0)
POLABIAN = Language('polabian', __file__, 0, 5, extinct_year=1756)
POLISH = Language('polish', __file__, 40000000, 670000)
RUSSIAN = Language('russian', __file__, 150000000, 110000000)
RUSYN = Language('rusyn', __file__, 70000, 0)
SERBO_CROATIAN = Language('serbo_croatian', __file__, 19000000, 0)
SILESIAN = Language('silesian', __file__, 457900, 0)
SLOVAK = Language('slovak', __file__, 5000000, 2000000)
SLOVENE = Language('slovene', __file__, 2500000, 0)
SORBIAN_LOWER = Language('sorbian_lower', __file__, 6900, 0)
SORBIAN_UPPER = Language('sorbian_upper', __file__, 13000, 0)
UKRAINIAN = Language('ukrainian', __file__, 27000000, 5800000)

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
