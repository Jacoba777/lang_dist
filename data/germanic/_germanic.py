from model.lang import Language
from model.word import word_distance

FAMILY = 'germanic'

ENGLISH = Language('english', FAMILY, 372900000, 1080000000)
GERMAN = Language('german', FAMILY, 95000000, 83000000)
DUTCH = Language('dutch', FAMILY, 25000000, 5000000)
AFRIKAANS = Language('afrikaans', FAMILY, 7200000, 10300000)
SWEDISH = Language('swedish', FAMILY, 10000000, 3000000)
DANISH = Language('danish', FAMILY, 6000000, 0)
NORWEGIAN = Language('norwegian', FAMILY, 5000000, 0)
NORWEGIAN_NYNORSK = Language('norwegian_nynorsk', FAMILY, 5000000, 0)
SCOTS = Language('scots', FAMILY, 1540000, 0)
YIDDISH = Language('yiddish', FAMILY, 600000, 0)
WEST_FRISIAN = Language('west_frisian', FAMILY, 470000, 0)
LUXEMBOURGISH = Language('luxembourgish', FAMILY, 430000, 0)
ICELANDIC = Language('icelandic', FAMILY, 340000, 0)
FAROESE = Language('faroese', FAMILY, 69000, 0)
GOTHIC = Language('gothic', FAMILY, 0, 0)

ALL_LANGS = [
    ENGLISH,
    GERMAN,
    GOTHIC,
    DUTCH,
    AFRIKAANS,
    WEST_FRISIAN,
    LUXEMBOURGISH,
    YIDDISH,
    FAROESE,
    NORWEGIAN,
    NORWEGIAN_NYNORSK,
    ICELANDIC,
    SWEDISH,
    DANISH,
    SCOTS,
]

if __name__ == '__main__':
    word = 'black'
    word_en = ENGLISH.get_word(word)
    word_de = GERMAN.get_word(word)
    print(word_en, word_de, word_distance(word_en, word_de, debug=True))
