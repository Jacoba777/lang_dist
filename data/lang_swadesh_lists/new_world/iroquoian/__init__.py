from model.lang import Language

CHEROKEE = Language('cherokee', __file__, 1800)
ERIE = Language('erie', __file__, extinct_year=1600)
MOHAWK = Language('mohawk', __file__, 3900)
NOTTOWAY = Language('nottoway', __file__, extinct_year=1838)
WYANDOT = Language('wyandot', __file__, extinct_year=1972)

IROQUOIAN = [
    CHEROKEE,
    ERIE,
    MOHAWK,
    NOTTOWAY,
    WYANDOT,
]
