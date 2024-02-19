from model.lang import Language

ALTAI_NORTHERN = Language('altai_northern', __file__, 57000)
ALTAI_SOUTHERN = Language('altai_southern', __file__, 68700)
AZERBAIJANI = Language('azerbaijani', __file__, 24000000)
BASHKIR = Language('bashkir', __file__, 1200000)
CHAGATAI = Language('chagatai', __file__, extinct_year=1921)
CHUVASH = Language('chuvash', __file__, 740000)
KARACHAY_BALKAR = Language('karachay_balkar', __file__, 310000)
KARAKALPAK = Language('karakalpak', __file__, 870000)
KARAKHANID = Language('karakhanid', __file__, extinct_year=1000)
KAZAKH = Language('kazakh', __file__, 14000000)
KHAKAS = Language('khakas', __file__, 43000)
KUMYK = Language('kumyk', __file__, 450000)
KYRGYZ = Language('kyrgyz', __file__, 5150000)
NOGAI = Language('nogai', __file__, 86000)
SHOR = Language('shor', __file__, 2800)
TATAR = Language('tatar', __file__, 5200000)
TATAR_CRIMEAN = Language('tatar_crimean', __file__, 580000)
TATAR_SIBERIAN = Language('tatar_siberian', __file__, 100000)
TURKISH = Language('turkish', __file__, 84000000, 6000000)
TURKMEN = Language('turkmen', __file__, 6560000)
TUVAN = Language('tuvan', __file__, 240000)
URUM = Language('urum', __file__, 190000)
UYGHUR = Language('uyghur', __file__, 9500000)
UZBEK = Language('uzbek', __file__, 31000000)
YAKUT = Language('yakut', __file__, 450000)

TURKIC = [
    ALTAI_NORTHERN,
    ALTAI_SOUTHERN,
    AZERBAIJANI,
    BASHKIR,
    CHAGATAI,
    CHUVASH,
    KARACHAY_BALKAR,
    KARAKALPAK,
    KARAKHANID,
    KAZAKH,
    KHAKAS,
    KUMYK,
    KYRGYZ,
    NOGAI,
    SHOR,
    TATAR,
    TATAR_CRIMEAN,
    TATAR_SIBERIAN,
    TURKISH,
    TURKMEN,
    TUVAN,
    URUM,
    UYGHUR,
    UZBEK,
    YAKUT,
]
