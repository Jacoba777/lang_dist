from model.lang import Language
from model.word import word_distance

FAMILY = 'germanic'

ENGLISH = Language('english', FAMILY, 372900000, 1080000000)
GERMAN = Language('german', FAMILY, 95000000, 83000000)
GOTHIC = Language('gothic', FAMILY, 0, 0)

ALL_LANGS = [ENGLISH, GERMAN, GOTHIC]


if __name__ == '__main__':
    word = 'black'
    word_en = ENGLISH.get_word(word)
    word_de = GERMAN.get_word(word)
    print(word_en, word_de, word_distance(word_en, word_de, debug=True))
