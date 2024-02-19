from model.lang import Language

# NOTE: For extinct Afroasiatic languages, the exact pronunciation is lost because these languages often do not write vowels. Egyptian and Old Hebrew in particular are reconstructions

# AMAZIGH = Language('amazigh', _family, )  # I believe this language is a duplicate of CAT
AMHARIC = Language('amharic', __file__, 32000000, 25000000)
ARABIC_CYPRIOT = Language('arabic_cypriot', __file__, 900)
ARABIC_EGYPTIAN = Language('arabic_egyptian', __file__, 77000000, 25000000)
ARABIC_JUBA = Language('arabic_juba', __file__, 250000, 1200000)
ARABIC_LEVANTINE_SOUTH = Language('arabic_levantine_south', __file__, 47000000, 360000)  # All levantine speakers included
ARABIC_MOROCCAN = Language('arabic_moroccan', __file__, 30000000, 9600000)
ARABIC_STANDARD = Language('arabic_standard', __file__, 0, 270000000)
ARABIC_TUNISIAN = Language('arabic_tunisian', __file__, 12000000)
# TODO: Translate Sudanese, Chadian, N. Levantine, Mesopotamian, Peninsular, Central Asian, and Sa'idi Arabic dialects
# CENTRAL_ATLAS_TAMAZIGHT = Language('central_atlas_tamazight', _family, 4700000)  # todo Too many syllabic consonants, will have to revisit
EGYPTIAN_LATE = Language('egyptian_late', __file__, extinct_year=-800)
EGYPTIAN_MIDDLE = Language('egyptian_middle', __file__, extinct_year=-1400)
EGYPTIAN_OLD = Language('egyptian_old', __file__, extinct_year=-2000)
HAUSA = Language('hausa', __file__, 52000000, 27000000)
HEBREW_ASHKENAZI = Language('hebrew_ashkenazi', __file__)  # No data; Speakers are included in MIH
HEBREW_BIBLICAL = Language('hebrew_biblical', __file__, extinct_year=200)
HEBREW_MODERN_ISRAELI = Language('hebrew_modern_israeli', __file__, 5000000, 3300000)
HEBREW_SEPHARDI = Language('hebrew_sephardi', __file__)  # No data; Speakers are included in MIH
HEBREW_SYRIAN = Language('hebrew_syrian', __file__)  # No data; Speakers are included in MIH
HEBREW_TIBERIAN = Language('hebrew_tiberian', __file__, extinct_year=950)
HEBREW_YEMENITE = Language('hebrew_yemenite', __file__)  # No data; Speakers are included in MIH
MALTESE = Language('maltese', __file__, 570000)
MANDAIC_MODERN = Language('mandaic_modern', __file__, 150)
PHOENICIAN = Language('phoenician', __file__, extinct_year=-200)
SOMALI = Language('somali', __file__, 22000000)
SURET = Language('suret', __file__, 240000)
TASHELHIT = Language('tashelhit', __file__, 5800000)
TIGRINYA = Language('tigrinya', __file__, 8670000)


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
