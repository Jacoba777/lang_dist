from model.lang import Language

_family = 'constructed'

ESPERANTO = Language('esperanto', _family, 1000, 100000)
IDO = Language('ido', _family, 26, 150)
INTERLINGUA = Language('interlingua', _family, 0, 200)
INTERLINGUE = Language('interlingue', _family)  # No data on number of speakers
KLINGON = Language('klingon', _family, 0, 25)
LINGUA_FRANCA_NOVA = Language('lingua_franca_nova', _family)  # No data on number of speakers
LINGWA_DE_PLANETA = Language('lingwa_de_planeta', _family, 0, 25)
LOJBAN = Language('lojban', _family, 0, 5)
LAADAN = Language('láadan', _family, 0)  # No data on number of speakers
NEO = Language('neo', _family, 0)  # No data on number of speakers
NOVIAL = Language('novial', _family, 0)  # No data on number of speakers
TOKI_PONA = Language('toki_pona', _family, 0, 408)
VOLAPUK = Language('volapük', _family, 0, 20)


CONSTRUCTED = [
    ESPERANTO,
    IDO,
    INTERLINGUA,
    INTERLINGUE,
    KLINGON,
    LINGUA_FRANCA_NOVA,
    LINGWA_DE_PLANETA,
    LOJBAN,
    LAADAN,
    NEO,
    NOVIAL,
    TOKI_PONA,
    VOLAPUK,
]
