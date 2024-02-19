from model.lang import Language
from model.word import word_distance

ENGLISH_UK = Language('english_uk', __file__, 130900000, 1080000000)
ENGLISH_US = Language('english_us', __file__, 242000000, 1080000000)
ENGLISH_MIDDLE = Language('english_middle', __file__, extinct_year=1470)
ENGLISH_OLD = Language('english_old', __file__, extinct_year=1100)
GERMAN = Language('german', __file__, 95000000, 83000000)
DUTCH = Language('dutch', __file__, 25000000, 5000000)
AFRIKAANS = Language('afrikaans', __file__, 7200000, 10300000)
SWEDISH = Language('swedish', __file__, 10000000, 3000000)
DANISH = Language('danish', __file__, 6000000, 0)
GERMAN_LOW = Language('german_low', __file__, 5900000, 10000000)
NORWEGIAN_BOKMAL = Language('norwegian_bokmal', __file__, 3670000, 0)
SCOTS = Language('scots', __file__, 1540000, 0)
LIMBURGISH = Language('limburgish', __file__, 1300000)
NORWEGIAN_NYNORSK = Language('norwegian_nynorsk', __file__, 650000, 0)
YIDDISH = Language('yiddish', __file__, 600000, 0)
WEST_FRISIAN = Language('west_frisian', __file__, 470000, 0)
LUXEMBOURGISH = Language('luxembourgish', __file__, 430000, 0)
FRANCONIAN_CENTRAL = Language('franconian_central', __file__, 360000)  # Using Lorraine Franconian numbers
ICELANDIC = Language('icelandic', __file__, 340000, 0)
ZEELANDIC = Language('zeelandic', __file__, 220000, 0)
FAROESE = Language('faroese', __file__, 69000, 0)
GOTHIC = Language('gothic', __file__, extinct_year=1700)

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
