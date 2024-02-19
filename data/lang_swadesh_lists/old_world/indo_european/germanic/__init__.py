from model.lang import Language
from model.word import word_distance

_FAMILY = 'germanic'

ENGLISH_UK = Language('english_uk', _FAMILY, 130900000, 1080000000)
ENGLISH_US = Language('english_us', _FAMILY, 242000000, 1080000000)
ENGLISH_MIDDLE = Language('english_middle', _FAMILY, extinct_year=1470)
ENGLISH_OLD = Language('english_old', _FAMILY, extinct_year=1100)
GERMAN = Language('german', _FAMILY, 95000000, 83000000)
DUTCH = Language('dutch', _FAMILY, 25000000, 5000000)
AFRIKAANS = Language('afrikaans', _FAMILY, 7200000, 10300000)
SWEDISH = Language('swedish', _FAMILY, 10000000, 3000000)
DANISH = Language('danish', _FAMILY, 6000000, 0)
GERMAN_LOW = Language('german_low', _FAMILY, 5900000, 10000000)
NORWEGIAN_BOKMAL = Language('norwegian_bokmal', _FAMILY, 3670000, 0)
SCOTS = Language('scots', _FAMILY, 1540000, 0)
LIMBURGISH = Language('limburgish', _FAMILY, 1300000)
NORWEGIAN_NYNORSK = Language('norwegian_nynorsk', _FAMILY, 650000, 0)
YIDDISH = Language('yiddish', _FAMILY, 600000, 0)
WEST_FRISIAN = Language('west_frisian', _FAMILY, 470000, 0)
LUXEMBOURGISH = Language('luxembourgish', _FAMILY, 430000, 0)
FRANCONIAN_CENTRAL = Language('franconian_central', _FAMILY, 360000)  # Using Lorraine Franconian numbers
ICELANDIC = Language('icelandic', _FAMILY, 340000, 0)
ZEELANDIC = Language('zeelandic', _FAMILY, 220000, 0)
FAROESE = Language('faroese', _FAMILY, 69000, 0)
GOTHIC = Language('gothic', _FAMILY, extinct_year=1700)

GERMANIC = [
    ENGLISH_UK,
    ENGLISH_US,
    ENGLISH_MIDDLE,
    ENGLISH_OLD,
    GERMAN,
    GOTHIC,
    DUTCH,
    AFRIKAANS,
    WEST_FRISIAN,
    LUXEMBOURGISH,
    YIDDISH,
    FAROESE,
    NORWEGIAN_BOKMAL,
    NORWEGIAN_NYNORSK,
    ICELANDIC,
    SWEDISH,
    DANISH,
    GERMAN_LOW,
    FRANCONIAN_CENTRAL,
    LIMBURGISH,
    SCOTS,
    ZEELANDIC,
]

if __name__ == '__main__':
    word = 'black'
    word_en = ENGLISH_US.get_word(word)
    word_de = GERMAN.get_word(word)
    print(word_en, word_de, word_distance(word_en, word_de, debug=True))
