from model.lang import Language

_FAMILY = 'turkic'

ALTAI_NORTHERN = Language('altai_northern', _FAMILY, 57000)
ALTAI_SOUTHERN = Language('altai_southern', _FAMILY, 68700)
AZERBAIJANI = Language('azerbaijani', _FAMILY, 24000000)
BASHKIR = Language('bashkir', _FAMILY, 1200000)
CHAGATAI = Language('chagatai', _FAMILY, extinct_year=1921)
CHUVASH = Language('chuvash', _FAMILY, 740000)
KARACHAY_BALKAR = Language('karachay_balkar', _FAMILY, 310000)
KARAKALPAK = Language('karakalpak', _FAMILY, 870000)
KARAKHANID = Language('karakhanid', _FAMILY, extinct_year=1000)
KAZAKH = Language('kazakh', _FAMILY, 14000000)
KHAKAS = Language('khakas', _FAMILY, 43000)
KUMYK = Language('kumyk', _FAMILY, 450000)
KYRGYZ = Language('kyrgyz', _FAMILY, 5150000)
NOGAI = Language('nogai', _FAMILY, 86000)
SHOR = Language('shor', _FAMILY, 2800)
TATAR = Language('tatar', _FAMILY, 5200000)
TATAR_CRIMEAN = Language('tatar_crimean', _FAMILY, 580000)
TATAR_SIBERIAN = Language('tatar_siberian', _FAMILY, 100000)
TURKISH = Language('turkish', _FAMILY, 84000000, 6000000)
TURKMEN = Language('turkmen', _FAMILY, 6560000)
TUVAN = Language('tuvan', _FAMILY, 240000)
URUM = Language('urum', _FAMILY, 190000)
UYGHUR = Language('uyghur', _FAMILY, 9500000)
UZBEK = Language('uzbek', _FAMILY, 31000000)
YAKUT = Language('yakut', _FAMILY, 450000)

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
