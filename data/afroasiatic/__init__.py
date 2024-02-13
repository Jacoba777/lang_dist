from model.lang import Language

_family = 'afroasiatic'

# NOTE: For extinct Afroasiatic languages, the exact pronunciation is lost because these languages often do not write vowels. Egyptian and Old Hebrew in particular are reconstructions

# AMAZIGH = Language('amazigh', _family, )  # I believe this language is a duplicate of CAT
AMHARIC = Language('amharic', _family, 32000000, 25000000)
ARABIC_CYPRIOT = Language('arabic_cypriot', _family, 900)
ARABIC_EGYPTIAN = Language('arabic_egyptian', _family, 77000000, 25000000)
ARABIC_JUBA = Language('arabic_juba', _family, 250000, 1200000)
ARABIC_LEVANTINE_SOUTH = Language('arabic_levantine_south', _family, 47000000, 360000)  # All levantine speakers included
ARABIC_MOROCCAN = Language('arabic_moroccan', _family, 30000000, 9600000)
ARABIC_STANDARD = Language('arabic_standard', _family, 0, 270000000)
ARABIC_TUNISIAN = Language('arabic_tunisian', _family, 12000000)
# TODO: Translate Sudanese, Chadian, N. Levantine, Mesopotamian, Peninsular, Central Asian, and Sa'idi Arabic dialects
# CENTRAL_ATLAS_TAMAZIGHT = Language('central_atlas_tamazight', _family, 4700000)  # todo Too many syllabic consonants, will have to revisit
EGYPTIAN_LATE = Language('egyptian_late', _family, extinct_year=-800)
EGYPTIAN_MIDDLE = Language('egyptian_middle', _family, extinct_year=-1400)
EGYPTIAN_OLD = Language('egyptian_old', _family, extinct_year=-2000)
HAUSA = Language('hausa', _family, 52000000, 27000000)
HEBREW_ASHKENAZI = Language('hebrew_ashkenazi', _family)  # No data; Speakers are included in MIH
HEBREW_BIBLICAL = Language('hebrew_biblical', _family, extinct_year=200)
HEBREW_MODERN_ISRAELI = Language('hebrew_modern_israeli', _family, 5000000, 3300000)
HEBREW_SEPHARDI = Language('hebrew_sephardi', _family)  # No data; Speakers are included in MIH
HEBREW_SYRIAN = Language('hebrew_syrian', _family)  # No data; Speakers are included in MIH
HEBREW_TIBERIAN = Language('hebrew_tiberian', _family, extinct_year=950)
HEBREW_YEMENITE = Language('hebrew_yemenite', _family)  # No data; Speakers are included in MIH
MALTESE = Language('maltese', _family, 570000)
MANDAIC_MODERN = Language('mandaic_modern', _family, 150)
PHOENICIAN = Language('phoenician', _family, extinct_year=-200)
SOMALI = Language('somali', _family, 22000000)
SURET = Language('suret', _family, 240000)
TASHELHIT = Language('tashelhit', _family, 5800000)
TIGRINYA = Language('tigrinya', _family, 8670000)


AFROASIATIC = [
    # AMAZIGH,
    AMHARIC,
    ARABIC_CYPRIOT,
    ARABIC_EGYPTIAN,
    ARABIC_JUBA,
    ARABIC_LEVANTINE_SOUTH,
    ARABIC_MOROCCAN,
    ARABIC_STANDARD,
    ARABIC_TUNISIAN,
    # CENTRAL_ATLAS_TAMAZIGHT,
    EGYPTIAN_LATE,
    EGYPTIAN_MIDDLE,
    EGYPTIAN_OLD,
    HAUSA,
    HEBREW_ASHKENAZI,
    HEBREW_BIBLICAL,
    HEBREW_MODERN_ISRAELI,
    HEBREW_SEPHARDI,
    HEBREW_SYRIAN,
    HEBREW_TIBERIAN,
    HEBREW_YEMENITE,
    MALTESE,
    MANDAIC_MODERN,
    PHOENICIAN,
    SOMALI,
    SURET,
    TASHELHIT,
    TIGRINYA,
]
