from model.state_word import get_syllable_list_dist
from model.syllable import create_syllables_from_ipa_string


# still need to add word to weighted lev 2 and refactor to use this instead of strings
class Word:
    def __init__(self, native: str = '', romanized: str = '', ipa: str = ''):
        self.native = native
        self.romanized = romanized
        self.ipa = ipa
        self.ipa_tokenized = create_syllables_from_ipa_string(ipa)

    def __repr__(self):
        return f'<Word "{self.native} /{self.ipa}/">'


def word_distance(w1: Word, w2: Word, debug=False):
    try:
        return get_syllable_list_dist(w1.ipa_tokenized, w2.ipa_tokenized, debug=debug)
    except Exception as ex:
        raise Exception(f'Failed to compare {w1} to {w2}', ex)


def main():
    word1 = Word(ipa='kæt')
    word2 = Word(ipa='ʃa')


if __name__ == '__main__':
    main()
