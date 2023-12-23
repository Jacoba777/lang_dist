import os
from typing import Dict

from model.word import Word
from config import ROOT


class Language:
    def __init__(self, name: str, family: str, native_speakers: int, l2_speakers: int):
        self.name = name
        self.family = family
        self._create_dict_from_raw_data()

        self.native_speakers = native_speakers
        self.l2_speakers = l2_speakers
        self.total_speakers = native_speakers + l2_speakers

    def _create_dict_from_raw_data(self):
        self._dict = {}

        swadesh_loc = os.path.join(ROOT, 'data', 'swadesh.txt')
        with open(swadesh_loc) as f:
            swadesh_words = f.read().split('\n')

        filename = f'{self.name}.txt'
        path = os.path.join(ROOT, 'data', self.family, filename)
        with open(path, encoding='UTF-8') as f:
            word_data = f.read().split('\n')

        words_zip = zip(swadesh_words, word_data)

        for word_swadesh, word_lang_data in words_zip:
            word_fields = word_lang_data.split('\t')
            if len(word_fields) != 3:
                raise ValueError(f'Malformed Data Line for {self.name}: "{word_fields}"')
            self._dict[word_swadesh] = Word(*word_fields)

    def get_all_words(self):
        return self._dict.values()

    def get_word(self, word: str):
        return self._dict.get(word, None)

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name


def get_lang_data():
    with open('lang.txt', encoding="UTF-8") as f:
        data = f.read()
        for s in [' ', '(', ')', '-', '.', '²', '¹', 'ʰ', 'ʷ', 'ˀ', 'ˈ', 'ˌ', 'ː', 'ˑ', 'ˢ', '˦', '˨', '̂', '̃', '̈', '̊', '̚', '̞', '̟', '̠', '̥', '̩', '̪', '̯', '̹', '̽', '͈', '͡', '⁽', '⁾']:
            data = data.replace(s, '')
        data = data.split('\n')

    langs: Dict[int, Language] = {i: Language(name, 'germanic', 0, 0) for i, name in enumerate(data[0].split('\t'))}
    for word_row in data[1:]:
        word_en = word_row.split('\t')[0]
        for i, word in enumerate(word_row.split('\t')):
            langs.get(i).set_word(word_en, word)
    return list(langs.values())
