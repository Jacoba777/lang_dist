import os
from typing import Dict

from model.word import Word
from config import ROOT


class Language:
    def __init__(self, name: str, family: str | None, native_speakers: int = 0, l2_speakers: int = 0, extinct_year: int | None = None):
        self.name = name
        self.family = family
        self.extinct_year = extinct_year
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

    def get_word_count(self, word_type='ipa_tokenized'):
        return len([word.ipa for word in self.get_all_words() if word.__getattribute__(word_type) is not None])

    def get_embarrassment_level(self):
        num_ipa_words = len([word.ipa for word in self.get_all_words() if word.ipa_tokenized is not None])
        return ((207 - num_ipa_words) * self.total_speakers) / 1000000

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name
