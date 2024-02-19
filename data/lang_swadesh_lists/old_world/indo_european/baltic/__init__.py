from model.lang import Language

LATGALIAN = Language('latgalian', __file__, 200000, 0)
LATVIAN = Language('latvian', __file__, 1500000, 0)
LITHUANIAN = Language('lithuanian', __file__, 3000000, 0)
PRUSSIAN_OLD = Language('prussian_old', __file__, extinct_year=1700)
SAMOGITIAN = Language('samogitian', __file__, 500000, 0)


BALTIC = [
    LATGALIAN,
    LATVIAN,
    LITHUANIAN,
    PRUSSIAN_OLD,
    SAMOGITIAN,
]
