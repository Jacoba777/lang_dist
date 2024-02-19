from model.lang import Language

CAHUILLA = Language('cahuilla', __file__, 6)
HOPI = Language('hopi', __file__, 6100)
HUICHOL = Language('huichol', __file__, 60000)
NAHUATL_CENTRAL = Language('nahuatl_central', __file__, 200000)  # My guess. This covers Guerrero and several other dialects
NAHUATL_CLASSICAL = Language('nahuatl_classical', __file__, extinct_year=1500)
NAHUATL_GUERRERO = Language('nahuatl_guerrero', __file__, 125000)
NAHUATL_HUASTECA_CENTRAL = Language('nahuatl_huasteca_central', __file__, 200000)
NAHUATL_HUASTECA_EASTERN = Language('nahuatl_huasteca_eastern', __file__, 410000)
NAHUATL_HUASTECA_WESTERN = Language('nahuatl_huasteca_western', __file__, 400000)
NAHUATL_TEMASCALTEPEC = Language('nahuatl_temascaltepec', __file__, 310)
OODHAM = Language('oodham', __file__, 15000)
PIPIL = Language('pipil', __file__, 500)
SHOSHONE = Language('shoshone', __file__, 1000)
TONGVA = Language('tongva', __file__, extinct_year=1900)
UTE = Language('ute', __file__, 1640)
YAQUI = Language('yaqui', __file__, 20600)


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
