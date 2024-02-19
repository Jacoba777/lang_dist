import os

from data.swadesh import SWADESH_WORDS
from model.word import Word


class Language:
    def __init__(self, name: str, _file: str | None, native_speakers: int = 0, l2_speakers: int = 0, extinct_year: int | None = None):
        self.name = name
        self.family = _file.split('\\')[-2]
        self.extinct_year = extinct_year
        self._create_dict_from_raw_data(_file)

        self.native_speakers = native_speakers
        self.l2_speakers = l2_speakers
        self.total_speakers = native_speakers + l2_speakers

    def _create_dict_from_raw_data(self, _file: str):
        self._dict = {}

        word_data = _get_data_loc_from_file(_file, self.name)
        words_zip = zip(SWADESH_WORDS, word_data)

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
        return ((207 - self.get_word_count('ipa')) * self.total_speakers) / 1000000

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name


def _get_data_loc_from_file(_file: str, lang_name: str):
    relpath = os.path.relpath(_file, os.getcwd())
    path_parts = relpath.split('\\')[:-1]  # Remove the file name from path
    dir_loc = '\\'.join(path_parts)

    filename = f'{lang_name}.txt'
    path = os.path.join(dir_loc, filename)
    with open(path, encoding='UTF-8') as f:
        word_data = f.read().split('\n')

    return word_data
