from model.lang import Language

_family = 'uto_aztecan'

CAHUILLA = Language('cahuilla', _family, 6)
HOPI = Language('hopi', _family, 6100)
HUICHOL = Language('huichol', _family, 60000)
NAHUATL_CENTRAL = Language('nahuatl_central', _family, 200000)  # My guess. This covers Guerrero and several other dialects
NAHUATL_CLASSICAL = Language('nahuatl_classical', _family, extinct_year=1500)
NAHUATL_GUERRERO = Language('nahuatl_guerrero', _family, 125000)
NAHUATL_HUASTECA_CENTRAL = Language('nahuatl_huasteca_central', _family, 200000)
NAHUATL_HUASTECA_EASTERN = Language('nahuatl_huasteca_eastern', _family, 410000)
NAHUATL_HUASTECA_WESTERN = Language('nahuatl_huasteca_western', _family, 400000)
NAHUATL_TEMASCALTEPEC = Language('nahuatl_temascaltepec', _family, 310)
OODHAM = Language('oodham', _family, 15000)
PIPIL = Language('pipil', _family, 500)
SHOSHONE = Language('shoshone', _family, 1000)
TONGVA = Language('tongva', _family, extinct_year=1900)
UTE = Language('ute', _family, 1640)
YAQUI = Language('yaqui', _family, 20600)


UTO_AZTECAN = [
    CAHUILLA,
    HOPI,
    HUICHOL,
    NAHUATL_CENTRAL,
    NAHUATL_CLASSICAL,
    NAHUATL_GUERRERO,
    NAHUATL_HUASTECA_CENTRAL,
    NAHUATL_HUASTECA_EASTERN,
    NAHUATL_HUASTECA_WESTERN,
    NAHUATL_TEMASCALTEPEC,
    OODHAM,
    PIPIL,
    SHOSHONE,
    TONGVA,
    UTE,
    YAQUI,
]
