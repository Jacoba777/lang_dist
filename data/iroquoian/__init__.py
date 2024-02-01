from model.lang import Language

_FAMILY = 'iroquoian'

CHEROKEE = Language('cherokee', _FAMILY, 1800)
ERIE = Language('erie', _FAMILY, extinct_year=1600)
MOHAWK = Language('mohawk', _FAMILY, 3900)
NOTTOWAY = Language('nottoway', _FAMILY, extinct_year=1838)
WYANDOT = Language('wyandot', _FAMILY, extinct_year=1972)

IROQUOIAN = [
    CHEROKEE,
    ERIE,
    MOHAWK,
    NOTTOWAY,
    WYANDOT,
]
