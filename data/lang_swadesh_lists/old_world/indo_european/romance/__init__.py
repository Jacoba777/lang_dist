from model.lang import Language

SPANISH = Language('spanish', __file__, 500000000, 100000000)
# PORTUGUESE = Language('portuguese', FAMILY, 230000000, 25000000)
PORTUGUESE_PT = Language('portuguese_pt', __file__, 0, 0)
PORTUGUESE_BR = Language('portuguese_br', __file__, 0, 0)
PORTUGUESE_OLD = Language('portuguese_old', __file__, extinct_year=1400)
FRENCH = Language('french', __file__, 81000000, 229000000)
FRENCH_OLD = Language('french_old', __file__, extinct_year=1350)
ITALIAN = Language('italian', __file__, 65000000, 3100000)
ROMANIAN = Language('romanian', __file__, 24000000, 4000000)
CATALAN = Language('catalan', __file__, 4100000, 5100000)
NEAPOLITAN = Language('neapolitan', __file__, 5700000, 0)
SICILIAN = Language('sicilian', __file__, 4700000, 0)
GALICIAN = Language('galician', __file__, 2400000, 0)
PIEDMONTESE = Language('piedmontese', __file__, 2000000, 0)
SARDINIAN = Language('sardinian', __file__, 1000000, 0)
LIGURIAN = Language('ligurian', __file__, 600000, 0)
FRIULIAN = Language('friulian', __file__, 420000, 180000)
WALLOON = Language('walloon', __file__, 300000, 300000)
OCCITAN = Language('occitan', __file__, 200000, 200000)
ROMANSH = Language('romansh', __file__, 60000, 0)

ARAGONESE = Language('aragonese', __file__, 11000, 30000)
AROMANIAN = Language('aromanian', __file__, 210000, 0)
ASTURIAN = Language('asturian', __file__, 100000, 450000)
DALMATIAN = Language('dalmatian', __file__, extinct_year=1898)
LATIN = Language('latin', __file__, 0, 2000, extinct_year=700)
OCCITAN_GASCON = Language('occitan_gascon', __file__, 250000, 0)
OCCITAN_LANGUEDOCIEN = Language('occitan_languedocien', __file__, 300000, 0)
ROMANIAN_ISTRO = Language('romanian_istro', __file__, 300, 1100)
ROMANIAN_MEGLENO = Language('romanian_megleno', __file__, 5000, 0)
SPANISH_OLD = Language('spanish_old', __file__, extinct_year=1400)

ROMANCE = [
    FRENCH,
    FRENCH_OLD,
    SPANISH,
    PORTUGUESE_PT,
    PORTUGUESE_BR,
    PORTUGUESE_OLD,
    ITALIAN,
    SICILIAN,
    GALICIAN,
    ROMANIAN,
    CATALAN,
    OCCITAN,
    NEAPOLITAN,
    LIGURIAN,
    PIEDMONTESE,
    SARDINIAN,
    ROMANSH,
    WALLOON,
    FRIULIAN,
    ARAGONESE,
    AROMANIAN,
    ASTURIAN,
    DALMATIAN,
    LATIN,
    OCCITAN_GASCON,
    OCCITAN_LANGUEDOCIEN,
    ROMANIAN_ISTRO,
    ROMANIAN_MEGLENO,
    SPANISH_OLD,
]
