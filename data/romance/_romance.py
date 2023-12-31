from model.lang import Language

FAMILY = 'romance'

SPANISH = Language('spanish', FAMILY, 500000000, 100000000)
PORTUGUESE = Language('portuguese', FAMILY, 230000000, 25000000)
FRENCH = Language('french', FAMILY, 81000000, 229000000)
ITALIAN = Language('italian', FAMILY, 65000000, 3100000)
ROMANIAN = Language('romanian', FAMILY, 24000000, 4000000)
CATALAN = Language('catalan', FAMILY, 4100000, 5100000)
NEAPOLITAN = Language('neapolitan', FAMILY, 5700000, 0)
SICILIAN = Language('sicilian', FAMILY, 4700000, 0)
GALICIAN = Language('galician', FAMILY, 2400000, 0)
PIEDMONTESE = Language('piedmontese', FAMILY, 2000000, 0)
SARDINIAN = Language('sardinian', FAMILY, 1000000, 0)
LIGURIAN = Language('ligurian', FAMILY, 600000, 0)
OCCITAN = Language('occitan', FAMILY, 200000, 0)

ALL_LANGS = [
    FRENCH,
    SPANISH,
    PORTUGUESE,
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
]
