from model.syllable import create_syllables_from_ipa_string


# still need to add word to weighted lev 2 and refactor to use this instead of strings
class Word:
    def __init__(self, native: str = '', romanized: str = '', ipa: str = ''):
        self.native = native
        self.romanized = romanized
        self.ipa = ipa
        self.ipa_tokenized = create_syllables_from_ipa_string(ipa)

    def __repr__(self):
        return f'<Word "{self.native}">'


def main():
    word1 = Word(ipa='kæt')
    word2 = Word(ipa='ʃa')


if __name__ == '__main__':
    main()
