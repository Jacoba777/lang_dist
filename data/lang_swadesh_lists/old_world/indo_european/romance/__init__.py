from model.lang import Language

_FAMILY = 'romance'

SPANISH = Language('spanish', _FAMILY, 500000000, 100000000)
# PORTUGUESE = Language('portuguese', FAMILY, 230000000, 25000000)
PORTUGUESE_PT = Language('portuguese_pt', _FAMILY, 0, 0)
PORTUGUESE_BR = Language('portuguese_br', _FAMILY, 0, 0)
PORTUGUESE_OLD = Language('portuguese_old', _FAMILY, extinct_year=1400)
FRENCH = Language('french', _FAMILY, 81000000, 229000000)
FRENCH_OLD = Language('french_old', _FAMILY, extinct_year=1350)
ITALIAN = Language('italian', _FAMILY, 65000000, 3100000)
ROMANIAN = Language('romanian', _FAMILY, 24000000, 4000000)
CATALAN = Language('catalan', _FAMILY, 4100000, 5100000)
NEAPOLITAN = Language('neapolitan', _FAMILY, 5700000, 0)
SICILIAN = Language('sicilian', _FAMILY, 4700000, 0)
GALICIAN = Language('galician', _FAMILY, 2400000, 0)
PIEDMONTESE = Language('piedmontese', _FAMILY, 2000000, 0)
SARDINIAN = Language('sardinian', _FAMILY, 1000000, 0)
LIGURIAN = Language('ligurian', _FAMILY, 600000, 0)
FRIULIAN = Language('friulian', _FAMILY, 420000, 180000)
WALLOON = Language('walloon', _FAMILY, 300000, 300000)
OCCITAN = Language('occitan', _FAMILY, 200000, 200000)
ROMANSH = Language('romansh', _FAMILY, 60000, 0)

ARAGONESE = Language('aragonese', _FAMILY, 11000, 30000)
AROMANIAN = Language('aromanian', _FAMILY, 210000, 0)
ASTURIAN = Language('asturian', _FAMILY, 100000, 450000)
DALMATIAN = Language('dalmatian', _FAMILY, extinct_year=1898)
LATIN = Language('latin', _FAMILY, 0, 2000, extinct_year=700)
OCCITAN_GASCON = Language('occitan_gascon', _FAMILY, 250000, 0)
OCCITAN_LANGUEDOCIEN = Language('occitan_languedocien', _FAMILY, 300000, 0)
ROMANIAN_ISTRO = Language('romanian_istro', _FAMILY, 300, 1100)
ROMANIAN_MEGLENO = Language('romanian_megleno', _FAMILY, 5000, 0)
SPANISH_OLD = Language('spanish_old', _FAMILY, extinct_year=1400)

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
