from model.lang import Language

ESPERANTO = Language('esperanto', __file__, 1000, 100000)
IDO = Language('ido', __file__, 26, 150)
INTERLINGUA = Language('interlingua', __file__, 0, 200)
INTERLINGUE = Language('interlingue', __file__)  # No data on number of speakers
KLINGON = Language('klingon', __file__, 0, 25)
LINGUA_FRANCA_NOVA = Language('lingua_franca_nova', __file__)  # No data on number of speakers
LINGWA_DE_PLANETA = Language('lingwa_de_planeta', __file__, 0, 25)
LOJBAN = Language('lojban', __file__, 0, 5)
LAADAN = Language('láadan', __file__, 0)  # No data on number of speakers
NEO = Language('neo', __file__, 0)  # No data on number of speakers
NOVIAL = Language('novial', __file__, 0)  # No data on number of speakers
TOKI_PONA = Language('toki_pona', __file__, 0, 408)
VOLAPUK = Language('volapük', __file__, 0, 20)


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
