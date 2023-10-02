from typing import Dict


class Language:
    def __init__(self, name):
        self.name = name
        self._dict = {}

    def set_word(self, word_in_en: str, word: str):
        self._dict[word_in_en] = word

    def get_word(self, word_in_en: str) -> str:
        if word_in_en not in self._dict:
            print('Missing word:', word_in_en, 'in', self.name)
            print('en_dict:', self._dict)
        return self._dict[word_in_en]

    def get_all_words(self):
        return self._dict.values()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.name < other.name


def get_lang_data():
    with open('lang.txt', encoding="UTF-8") as f:
        data = f.read()
        for s in [' ', '(', ')', '-', '.', '²', '¹', 'ã', 'ê', 'õ', 'ɕ', 'ɧ', 'ɫ', 'ʑ', 'ʧ', 'ʰ', 'ʷ', 'ˀ', 'ˈ', 'ˌ', 'ː', 'ˑ', 'ˢ', '˦', '˨', '̂', '̃', '̈', '̊', '̚', '̞', '̟', '̠', '̥', '̩', '̪', '̯', '̹', '̽', '͈', '͡', '⁽', '⁾']:
            data = data.replace(s, '')
        data = data.split('\n')

    langs: Dict[int, Language] = {i: Language(name) for i, name in enumerate(data[0].split('\t'))}
    for word_row in data[1:]:
        word_en = word_row.split('\t')[0]
        for i, word in enumerate(word_row.split('\t')):
            langs.get(i).set_word(word_en, word)
    return list(langs.values())
